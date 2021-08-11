from django.contrib.auth import authenticate, get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from accounts.models import RiddanceProfile
from core.forms import BootstrapFormMixin

UserModel = get_user_model()


class UserLoginForm(BootstrapFormMixin, forms.Form):
    user = None
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],

        )
        if not self.user:
            raise ValidationError('Email and/or password is incorrect')

    def save(self):
        return self.user


class UserRegisterForm(BootstrapFormMixin, UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class RiddanceProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = RiddanceProfile
        exclude = ('user', )


