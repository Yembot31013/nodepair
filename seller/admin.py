from django.contrib import admin, admindocs
from .models import *

# Register your models here.
class Languages_classAdmin(admin.StackedInline):
    model = Languages
    
class Professional_Info_classAdmin(admin.StackedInline):
    model = Professional_Info

class Occupation_classAdmin(admin.StackedInline):
    model = Occupation

class Skill_classAdmin(admin.StackedInline):
    model = Skill

class Education_classAdmin(admin.StackedInline):
    model = Education

class Certification_classAdmin(admin.StackedInline):
    model = Certification

class Linked_Accounts_classAdmin(admin.StackedInline):
    model = Linked_Accounts

class Account_Security_classAdmin(admin.StackedInline):
    model = Account_Security


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_Name', 'seller_mode','slug',)
    search_fields = ('full_Name', 'description',)
    fieldsets = (
        ('Personal Info', {
            "fields": (
                'full_Name', 'avatar', 'description', 'slogan', 'seller_mode', 'slug', 'is_seller'
            ),
        }),
    )
    inlines = [Languages_classAdmin, Occupation_classAdmin, Skill_classAdmin, Education_classAdmin, Certification_classAdmin, Professional_Info_classAdmin, Linked_Accounts_classAdmin, Account_Security_classAdmin]

admin.site.register(Personal_Info, ProfileAdmin)
admin.site.register(Language_Levels)
admin.site.register(Occupation_list)
admin.site.register(Skill_list)
admin.site.register(Skill_Levels)