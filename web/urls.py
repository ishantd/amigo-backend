from django.urls import path

from web import views


urlpatterns = [
    path('login/', views.index, name='index')
]