from django.contrib import admin
from .models import Meta_Order,  Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('buyer_address', 'payment_hash','smart_contract','payed_at','created_at',)
    date_hierarchy = "created_at"
    search_fields = ('buyer_address', 'payment_hash')
    list_per_page = 10
    list_filter = ('buyer_address',)


class MetaOrder(admin.ModelAdmin):
    list_display = ('order_id', 'status','completed','received','created_at',)
    date_hierarchy = "created_at"
    search_fields = ('order_id', 'status', 'service__title')
    list_per_page = 10
    list_filter = ('status',)

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Meta_Order, MetaOrder)
