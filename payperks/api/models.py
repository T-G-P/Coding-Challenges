from django.db import models

from django.contrib.auth.models import User

from random import randint


class UserProfile(models.Model):

    USER_TYPES = (
	('0', 'user'),
	('1', 'admin'),
    )
    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=1, choices=USER_TYPES, default=0)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    street = models.CharField(max_length=200)


class Sweep(models.Model):

    __PRIZE_RANGE = (1, 100)
    __PRIZE_AMOUNT_RANGE = (1000, 1000000)

    num_prizes = models.IntegerField(default=self.__gen_random_prize_num)
    prize_amount = models.IntegerField(default=self.__gen_random_prize_amount)
    winners = models.ManyToManyField(User)

    def __gen_random_prize_num():

        return randint(*self.__PRIZE_RANGE)

    def __gen_random_prize_num():

        return randint(*self.__PRIZE_AMOUNT_RANGE)

class Drawing(models.Model):

    user = models.ForeignKey(User)
    sweep = models.ForeignKey(User)
