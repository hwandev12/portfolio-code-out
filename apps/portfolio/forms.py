from django import forms
from .models import Contact


class ContactUsModelForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            "your_name",
            "email",
            "message",
            "category"
        )
