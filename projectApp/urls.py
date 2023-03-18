from django.urls import path
from . import views

urlpatterns = [
    path('fetchProject', views.fetchProject.as_view()),
    path('fetchRateProject', views.fetchRateProject.as_view()),
    path('projectDetail/<str:query>', views.projectDetailApiView),
    path('recProject', views.recommendedProject),
    path('rateProject', views.rateProject),
    path('profileProject/<int:query>/', views.profileProject),
    path('productProject/', views.productProject),
]
