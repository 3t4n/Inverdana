from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import *

class AuthForm(AdminAuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','autofocus':'form-control','class':'form-control'}),
    )
