from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from allauth.socialaccount.models import SocialAccount

from django.dispatch.dispatcher import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    profile_picture_url = models.URLField(max_length=2000, null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        p = Profile.objects.create(user=instance)
        
        
