from django import forms
from django.contrib.auth import get_user_model
from .models import Contact

User = get_user_model()


class ContactUsModelForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            "your_name",
            "email",
            "message",
        )
