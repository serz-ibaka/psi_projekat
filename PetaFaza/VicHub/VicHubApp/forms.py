from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, DateInput, PasswordInput, EmailInput

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth']
        widgets = {
            'username': TextInput(attrs={'class': 'data', 'placeholder': 'Korisnicko ime...'}),
            'email': EmailInput(attrs={'class': 'data', 'placeholder': 'example@mail.com'}),
            'password1': PasswordInput(attrs={'class': 'data'}),
            'password2': PasswordInput(attrs={'class': 'data'}),
            'first_name': TextInput(attrs={'class': 'data', 'placeholder': 'Ime...'}),
            'last_name': TextInput(attrs={'class': 'data', 'placeholder': 'Prezime...'}),
            'date_of_birth': DateInput(attrs={'class': 'data'})
        }

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.subscribed = 'N'
        user.status = 'A'
        user.type = 'U'
        if commit:
            user.save()
        return user