from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError, models, router, transaction

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, related_name= 'user_profile', on_delete=models.CASCADE,  primary_key=True)
    profile_pic=models.ImageField( upload_to='profile_pics')