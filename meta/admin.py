from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

class Pricing_classAdmin(admin.StackedInline):
    model = Pricing
class search_keyword_classAdmin(admin.StackedInline):
    model = search_keyword

class FAQ_classAdmin(admin.StackedInline):
    model = FAQ

class Service_offer_classAdmin(admin.StackedInline):
    model = Service_offer

class Gallery_classAdmin(admin.StackedInline):
    model = Gallery

class Pdf_classAdmin(admin.StackedInline):
    model = Pdf

class Publish_classAdmin(admin.StackedInline):
    model = Publish


class OverviewAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'title', 'category', 'sub_category', 'description', 'requirement', 'video', 'progress'
            ),
        }),
    )
    inlines = [Pricing_classAdmin, search_keyword_classAdmin, Service_offer_classAdmin, FAQ_classAdmin, Gallery_classAdmin, Pdf_classAdmin, Publish_classAdmin]

admin.site.register(Overview, OverviewAdmin)

admin.site.register(Category)
admin.site.register(Sub_Category)
