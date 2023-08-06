from django.urls import path

from home import create_meta, fetch
from home import views

urlpatterns = [
    path('', views.home, name="homes"),
    path('alter', views.change, name="switch"), # type: ignore
    path('listLanguage', fetch.search_language),
    path('listOccupation', fetch.search_occupation),
    path('listSkill', fetch.search_skill),
    path('listSkillLevel', fetch.skill_level),
    path('listcategory', fetch.search_category),
    path('listsubcategory', fetch.search_subcategory),

    # Url for searching meta & project according to query parameter
    path('query/<str:query>/', views.query_search, name="query"),
    # Url for fetching more meta & project on the home page according to the button clicked
    path('showAll/<str:show>/', views.showMore, name="showMore"),
    # project creation submit Url
    path('meta/s/project', create_meta.submitProjects, name="submitProjects"),
    # meta creation submit Url
    path('meta/s/meta', create_meta.create_meta, name="createMeta"),
    # payment package Url
    path('package/<int:pay_id>', views.payment_package, name="payment_package"),
    # subcribe Url
    path('subcribe', views.feedback), # type: ignore
    # create profile submit (json) Url
    path('soap', create_meta.create_profile),
    # create project Url
    path('meta/project', views.projects, name="project"),
    # create meta Url
    path('meta/metas', views.metas, name="metas"),
    # about the meta Url
    path('meta/<int:query>', views.about_meta, name="about_meta"),
    # about the meta Url
    path('meta/<int:query>', views.about_meta, name="about_meta"),
    # switch between meta and project creation Url
    path('meta', views.choice, name ="meta"),
    # login Url
    path('login/', views.loginpage, name="loginpage"),
    # register Url
    path('register/', views.register, name="register"),
    # logout Url
    path('logout/', views.logoutpage, name="logoutpage"),
]
