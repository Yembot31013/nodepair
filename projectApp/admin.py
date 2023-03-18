from django.contrib import admin
from .models import *

class Pricing_classAdmin(admin.StackedInline):
    model = Project_Pricing

class search_keyword_classAdmin(admin.StackedInline):
    model = Project_search_keyword

class FAQ_classAdmin(admin.StackedInline):
    model = Project_FAQ

class Gallery_classAdmin(admin.StackedInline):
    model = Project_Gallery

class Project_classAdmin(admin.StackedInline):
    model = Project_Project

class Publish_classAdmin(admin.StackedInline):
    model = Project_Publish


class OverviewAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'title', 'category', 'sub_category', 'description', 'video' , 'progress'
            ),
        }),
    )
    inlines = [Pricing_classAdmin, search_keyword_classAdmin, FAQ_classAdmin, Gallery_classAdmin, Project_classAdmin, Publish_classAdmin]

admin.site.register(Project_Overview, OverviewAdmin)

admin.site.register(Project_Category)
admin.site.register(Project_Sub_Category)

