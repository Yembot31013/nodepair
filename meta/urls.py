from django.urls import path
from . import views

urlpatterns = [
    path('fetchMeta', views.fetchMeta.as_view()),
    path('fetchRateMeta', views.fetchRateMeta.as_view()),
    path('metaDetail/<str:query>', views.metaDetailApiView),
    path('recMeta', views.recommendedMeta),
    path('rateMeta', views.rateMeta),
    # path('profileAll', views.profileAll),profileMeta
    path('profileMeta/<int:query>/', views.profileMeta),
    path('productMeta/', views.productMeta),
]
