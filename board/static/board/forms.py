from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from board.models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_title(self):
        title = self.cleaned_data['name']
        if len(title) > 255:
            raise ValidationError('Длина превышает 200 символов')
        return title
