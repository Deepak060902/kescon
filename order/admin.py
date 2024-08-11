from django.contrib import admin
from .models import Order, OrderItem, Shipment, Return

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class ShipmentInline(admin.TabularInline):
    model = Shipment
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_price', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline, ShipmentInline]

class ReturnAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'order__id')

admin.site.register(Order, OrderAdmin)
admin.site.register(Return, ReturnAdmin)
