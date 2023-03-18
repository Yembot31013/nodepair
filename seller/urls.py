from django.urls import path
from . import views, update_profile

urlpatterns = [
    path('home', views.home, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('order', views.order, name="order"),
    path('product', views.product, name="product"),
    path('customer', views.customer, name="customer"),
    path('tabs', views.iframeTab, name="iframeTab"),
    path('chatbot', views.chatbot, name="chatbot"),
    path('setting', views.settings, name="setting"),
    path('update_profile', update_profile.update_profile, name="update_profile"),
    path('update_pics', update_profile.update_pics, name="update_pics"),
    path('profile/<slug:name>', views.seller_info, name="seller_info"),
]
