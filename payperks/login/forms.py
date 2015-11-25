"""
Vast majority of code is taken and modified from here:
https://mayukhsaha.wordpress.com/2013/05/09/simple-login-and-user-registration-application-using-django/
"""


from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy


class RegistrationForm(forms.Form):

    username = forms.RegexField(
        regex=r'^\w+$',
        widget=forms.TextInput(
            attrs=dict(required=True, max_length=30)
        ),
        label=ugettext_lazy("Username"),
        error_messages={
            'invalid': ugettext_lazy(
                (
                    "This value must contain only"
                    "letters, numbers and underscores."
                )
            )
        }
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs=dict(required=True, max_length=30)
        ),
        label=ugettext_lazy("Email address")
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs=dict(
                required=True,
                max_length=30,
                render_value=False)
        ),
        label=ugettext_lazy("Password")
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs=dict(
                required=True,
                max_length=30,
                render_value=False
            )
        ),
        label=ugettext_lazy("Password (again)")
    )
    street = forms.CharField(
        widget=forms.TextInput(
            attrs=dict(
                required=True,
                max_length=128,
                render_value=False)
        ),
        label=ugettext_lazy("Street")
    )
    city = forms.CharField(
        widget=forms.TextInput(
            attrs=dict(
                required=True,
                max_length=128,
                render_value=False)
        ),
        label=ugettext_lazy("City")
    )
    state = forms.CharField(
        widget=forms.TextInput(
            attrs=dict(
                required=True,
                max_length=128,
                render_value=False)
        ),
        label=ugettext_lazy("State")
    )
    zip_code = forms.CharField(
        widget=forms.TextInput(
            attrs=dict(
                required=True,
                max_length=128,
                render_value=False)
        ),
        label=ugettext_lazy("Zip")
    )

    def clean_username(self):
        try:
            User.objects.get(
                username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(
            ugettext_lazy(
                (
                    "The username already exists."
                    "Please try another one."
                )
            )
        )

    def clean(self):
        if (
            'password1' in self.cleaned_data
            and 'password2' in self.cleaned_data
        ):
            if (
                self.cleaned_data['password1']
                != self.cleaned_data['password2']
            ):
                raise forms.ValidationError(
                    ugettext_lazy(
                        "The two password fields did not match."
                    )
                )
        return self.cleaned_data
