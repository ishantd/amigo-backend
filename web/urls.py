from django.urls import path

from web import views


urlpatterns = [
    path('login/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('shopify_callback/', views.shopify_callback, name='shopify_callback'),
    path('shopify_orders/', views.shopify_orders, name='shopify_orders'),
]