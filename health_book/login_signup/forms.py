from django import forms
from login_signup.models import User


class Connection1(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form__control btn btn--dark-green'}))

    class Meta:
        model = User
        fields = ['id_code', 'mail', 'password']
        widgets = {
            'id_code': forms.TextInput(attrs={
                'class': 'form__control btn btn--dark-green js-security-code',
                'placeholder': '0-00-00-00-000-000 0'
            }),
            'mail': forms.EmailInput(attrs={
                'class': 'form__control btn btn--dark-green',
                'placeholder': 'exemple@gmail.com'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form__control btn btn--dark-green',
                'autocomplete': 'false',
            }),
            'confirm_password': forms.PasswordInput(attrs={
                'class': 'form__control btn btn--dark-green',
                'autocomplete': 'false',
            })
        }


class LoginForm(forms.Form):

    id_code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form__control btn btn--dark-green js-security-code',
               'placeholder': '0-00-00-00-000-000 0'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form__control btn btn--dark-green',
               'autocomplete': 'false',
               'placeholder': 'password'}))
