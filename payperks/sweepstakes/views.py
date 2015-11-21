from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from sweepstakes.models import Sweep, Drawing
from .utils import admins_only, randint


@login_required
@require_http_methods(["POST"])
def earn_points(request):
    user = request.user
    drawing = user.drawing_set.latest('id')
    if drawing and drawing.is_open:
        response = {'status': 'You already have an open drawing'}

    else:
        new_drawing = Drawing(points=randint(0, 999999))
        user.drawing_set.add(new_drawing)
        response = {'status': new_drawing.points}

    return render_to_response('prize.html', response,)


@login_required
@admins_only
@require_http_methods(["POST"])
def run_sweeps(request):
    user = request.user

    new_sweep = Sweep()
    new_sweep.save()

    prize_amount = new_sweep.prize_amount
    num_prizes = new_sweep.num_prizes
    drawing_prize = prize_amount/num_prizes
    new_sweep.user = user

    drawings = Drawing.objects.filter(is_open=True)

    if drawings:
        new_sweep.drawing_set.add(*drawings.all())
        winning_drawings = drawings.\
            order_by('-points').\
            all()[:num_prizes]

        for drawing in drawings.all():
            if drawing in winning_drawings:
                drawing.is_winner = True
                drawing.prize_value = drawing_prize
            drawing.is_open = False
            drawing.save()
        response = {'status': 'Sweep Completed'}

    else:
        response = {'status': 'No drawings entered'}

    return render_to_response('sweeps.html', response,)


@login_required
@require_http_methods(["GET"])
def check_prize(request):
    user = request.user
    drawing = user.drawing_set.latest('id')

    if drawing.is_winner:
        response = {'status': 'You Won'}

    elif drawing.is_open:
        response = {'status': 'Drawing is still open'}

    else:
        response = {'status': 'You Lost'}

    return render_to_response('prize.html', response,)


@login_required
@require_http_methods(["POST"])
def claim_prize(request):
    user = request.user
    drawing = user.drawing_set.latest('id')

    if drawing.prize_claimed:
        response = {'status': 'Prize already claimed'}

    elif drawing.is_open:
        response = {'status': 'Drawing is still open'}

    elif not drawing.is_winner:
        response = {'status': 'You Lost'}

    else:
        drawing.prize_claimed = True
        drawing.save()
        address = '{} {} {}'.format(user.userprofile.street,
                                    user.userprofile.city,
                                    user.userprofile.state)
        response = {
            'status': 'Payment of {} sent to {}'.format(
                drawing.prize_value,
                address
            )
        }

    return render_to_response('prize.html', response,)
