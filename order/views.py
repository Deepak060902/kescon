from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Order, OrderItem, Shipment, Return
from cart.models import Cart, CartItem
from .forms import ReturnForm

@login_required
def place_order(request):
    cart = Cart.objects.get(user=request.user)
    if not cart.items.exists():
        return redirect('cart:view_cart')

    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address')
        billing_address = request.POST.get('billing_address')
        payment_method = request.POST.get('payment_method')

        order = Order.objects.create(
            user=request.user,
            total_price=cart.get_total_price(),
            status='Pending',
            shipping_address=shipping_address,
            billing_address=billing_address,
            payment_method=payment_method
        )

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.get_total_price()
            )

        cart.items.all().delete()
        return redirect('orders:order_summary', order_id=order.id)

    return render(request, 'place_order.html')

@login_required
def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_summary.html', {'order': order})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_history.html', {'orders': orders})

@login_required
def return_request(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            Return.objects.create(
                order=order,
                user=request.user,
                reason=form.cleaned_data['reason'],
                status='Requested'
            )
            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = ReturnForm()

    return render(request, 'return_request.html', {'form': form, 'order': order})
