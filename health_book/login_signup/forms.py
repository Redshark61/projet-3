from django import forms


class Connection1(forms.Form):

    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form__control btn btn--dark-green',
                                     'placeholder': 'First Name'
                                 }))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class': 'form__control btn btn--dark-green',
                                    'placeholder': 'First Name'
                                }))
    mail = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form__control btn btn--dark-green',
        'placeholder': 'exemple@gmail.com'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form__control btn btn--dark-green',
        'autocomplete': 'false',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form__control btn btn--dark-green',
        'autocomplete': 'false',
    }))


class LoginForm(forms.Form):

    id_code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form__control btn btn--dark-green js-security-code',
               'placeholder': '0-00-00-00-000-000 0'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form__control btn btn--dark-green',
               'autocomplete': 'false',
               'placeholder': 'password'}))
