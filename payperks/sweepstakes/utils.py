from random import randint


__PRIZE_RANGE = (1, 100)
__PRIZE_AMOUNT_RANGE = (1000, 1000000)


def gen_random_prize_num():
    return randint(*__PRIZE_RANGE)


def gen_random_prize_amount():
    return randint(*__PRIZE_AMOUNT_RANGE)
