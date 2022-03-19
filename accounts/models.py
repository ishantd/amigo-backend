from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.signals import pre_social_login

from django.dispatch.dispatcher import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    
@receiver(pre_social_login)
def social_login(request, sociallogin, **kwargs):
    user = sociallogin.user
    print(user, sociallogin)
    # try:
    #     user.profile.full_name
    # except Profile.DoesNotExist:
    #     Profile.objects.create(user=user)
