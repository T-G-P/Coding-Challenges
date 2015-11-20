from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from api.models import Sweep, Drawing
from django.contrib.auth.models import User
import json
import random


@require_http_methods(["POST"])
def earn_points(request, user_id):
    user = User.objects.get(id=user_id)
    drawing = user.drawing_set.first()
    if drawing and drawing.is_open:
        error = {'status': 'You already have an open drawing'}
        return HttpResponse(json.dumps(error),
                            content_type="application/json",
                            status=202)

    new_drawing = Drawing(points=random.randint(0, 999999))
    user.drawing_set.add(new_drawing)
    response = {'status': 'OK'}
    return HttpResponse(json.dumps(response),
                        content_type="application/json",
                        status=200)


@require_http_methods(["POST"])
def run_sweeps(request, user_id):
    user = User.objects.get(id=user_id)

    if not user.is_staff:
        error = {'status': 'Unauthorized'}
        return HttpResponse(json.dumps(error),
                            content_type="application/json",
                            status=404)

    new_sweep = Sweep()
    new_sweep.save()

    prize_amount = new_sweep.prize_amount
    num_prizes = new_sweep.num_prizes
    drawing_prize = prize_amount/num_prizes

    drawings = Drawing.objects.filter(is_open=True)
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


@require_http_methods(["GET"])
def check_prize(request, user_id, drawing_id):
    drawing = Drawing.query.filter(id=drawing_id).first()
    if drawing.user.id != user_id:
        error = {'status': 'Unauthorized'}
        return HttpResponse(json.dumps(error),
                            content_type="application/json",
                            status=404)
    elif drawing.is_winner:
        response = {'status': 'Won'}
        return HttpResponse(json.dumps(response),
                            content_type="application/json",
                            status=200)
    elif drawing.is_open:
        response = {'status': 'Open'}
        return HttpResponse(json.dumps(response),
                            content_type="application/json",
                            status=200)
    else:
        response = {'status': 'Lost'}
        return HttpResponse(json.dumps(response),
                            content_type="application/json",
                            status=200)


@require_http_methods(["POST"])
def claim_prize(request, user_id, drawing_id):
    drawing = Drawing.query.filter(id=drawing_id).first()
    if drawing.user.id != user_id:
        error = {'status': 'Unauthorized'}
        return HttpResponse(json.dumps(error),
                            content_type="application/json",
                            status=404)
    elif drawing.prize_claimed:
        error = {'status': 'Prize already claimed'}
        return HttpResponse(json.dumps(),
                            content_type="application/json",
                            status=200)
    elif drawing.is_open:
        error = {'status': 'Can\'t claim yet'}
        return HttpResponse(json.dumps(),
                            content_type="application/json",
                            status=200)
    elif not drawing.is_winner:
        error = {'status': 'Lost'}
        return HttpResponse(json.dumps(error),
                            content_type="application/json",
                            status=200)

    drawing.prize_claimed = True
    drawing.save()

    response = {'status': 'Payment of {} Sent'.format(drawing.prize_value)}
    return HttpResponse(json.dumps(response),
                        content_type="application/json",
                        status=200)
