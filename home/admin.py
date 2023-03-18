from django.contrib import admin
from .models import Message_Feedback, Available_Status

# Register your models here.

admin.site.register(Message_Feedback)
admin.site.register(Available_Status)