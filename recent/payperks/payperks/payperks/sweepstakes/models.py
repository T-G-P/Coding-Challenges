from django.db import models

from django.contrib.auth.models import User

from .utils import gen_random_prize_num, gen_random_prize_amount


class Sweep(models.Model):

    user = models.ForeignKey(User)
    num_prizes = models.IntegerField(default=gen_random_prize_num)
    prize_amount = models.IntegerField(default=gen_random_prize_amount)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)


class Drawing(models.Model):

    user = models.ForeignKey(User)
    sweep = models.ForeignKey(Sweep)
    points = models.IntegerField()
    is_open = models.BooleanField(default=True)
    is_winner = models.BooleanField(default=False)
    prize_claimed = models.BooleanField(default=False)
    prize_value = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
