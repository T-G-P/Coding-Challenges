"""
http://riceball.com/d/content/django-18-tutoria-52-adding-user-profile
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=200, blank=True)


def user_post_save(sender, instance, created, **kwargs):
    """Create a user profile when a new user account is created"""
    if created:
        user_profile = UserProfile()
        user_profile.user = instance
        user_profile.save()

post_save.connect(user_post_save, sender=User)
