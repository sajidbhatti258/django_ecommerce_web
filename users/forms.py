# users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customizing error messages for password validation
        self.fields['password1'].help_text = None  # Remove the default help text
        self.fields['password2'].help_text = None  # Remove the default help text
        self.fields['password1'].widget.attrs.update({'autocomplete': 'new-password'})
        self.fields['password2'].widget.attrs.update({'autocomplete': 'new-password'})

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        # You can add your own custom validation if needed here
        return password1
