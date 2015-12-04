from login.forms import User, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            user.userprofile.city = form.cleaned_data['city']
            user.userprofile.state = form.cleaned_data['state']
            user.userprofile.street = form.cleaned_data['street']
            user.userprofile.zip_code = form.cleaned_data['zip_code']
            user.userprofile.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form})

    return render_to_response('registration/register.html',
                              variables,)


def register_success(request):
    return render_to_response('registration/success.html',)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    if not request.user.is_staff:
        return render_to_response(
            'home.html',
            {'user': request.user}
        )
    return render_to_response(
        'admin.html',
        {'user': request.user}
    )
