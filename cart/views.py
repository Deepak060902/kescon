from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, CartItem
from .forms import AddToCartForm
import json 
from django.http import JsonResponse

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart_detail.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity += quantity
        cart_item.save()
        referer = request.META.get('HTTP_REFERER')

        if referer:
            return redirect(referer)
        else:
            return redirect('view_cart')
    else:
        form = AddToCartForm(instance=cart_item)
    
    return render(request, 'index.html', {'form': form, 'product': product})


@login_required
def update_cart_item(request, cart_item_id, new_quantity):
    try:
        order_item = CartItem.objects.get(id=cart_item_id)
        order_item.quantity = new_quantity
        order_item.save()

        return JsonResponse({'success': True})
    except CartItem.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'})

@login_required
def remove_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('view_cart')
