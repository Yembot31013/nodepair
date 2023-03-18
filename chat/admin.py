from django.contrib import admin
from .models import Thread, ChatMessage, Status


class ThreadAdmin(admin.ModelAdmin):
  list_display = ('id','timestamp', 'total_seller_unread','total_buyer_unread',)
  search_fields = ('id',)
class ChatAdmin(admin.ModelAdmin):
  list_display = ('user', 'unread','timestamp', "to")
  search_fields = ('user',)
class StatusAdmin(admin.ModelAdmin):
  list_display = ('profile', 'online','timestamp',)
  search_fields = ('profile',)

admin.site.register(Thread, ThreadAdmin)
admin.site.register(ChatMessage, ChatAdmin)
admin.site.register(Status, StatusAdmin)
