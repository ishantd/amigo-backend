from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    
