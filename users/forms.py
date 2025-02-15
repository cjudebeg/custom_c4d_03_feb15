from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

from accounts.models import CustomUser


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["displayname", "info"]
        widgets = {
            "displayname": forms.TextInput(attrs={"placeholder": "Add display name"}),
            "info": forms.Textarea(attrs={"rows": 3, "placeholder": "Add information"}),
        }


class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["email"]
