from random import randint
from functools import wraps
from django.http import HttpResponseRedirect


__PRIZE_RANGE = (1, 100)
__PRIZE_AMOUNT_RANGE = (1000, 1000000)


def gen_random_prize_num():
    return randint(*__PRIZE_RANGE)


def gen_random_prize_amount():
    return randint(*__PRIZE_AMOUNT_RANGE)


def admins_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):

        user = request.user
        if user.is_staff:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/home')

    return wrap


def users_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):

        user = request.user
        if not user.is_staff:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/home')

    return wrap
