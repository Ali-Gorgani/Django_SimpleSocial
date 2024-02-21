from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Username'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Email'}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm Password'}
        )
