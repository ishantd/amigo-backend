from django.urls import path

from accounts import views


urlpatterns = [
    path('dj-rest-auth/google/', views.GoogleLogin.as_view(), name='google_login')
]