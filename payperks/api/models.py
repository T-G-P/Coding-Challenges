from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):

    USER_TYPES = (
	('0', 'user'),
	('1', 'admin'),
    )
    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=1, choices=USER_TYPES, default=0)
    balance = models.IntegerField()

# class Sweep(models.Model):
#
#     num_prizes = models.IntegerField()
#     prize_amount = models.IntegerField()
#     winners = models.ManyToManyField(User)
