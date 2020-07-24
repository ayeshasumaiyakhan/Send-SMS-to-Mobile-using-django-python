
from django import forms
from .models import Contact_details
from django.forms import ModelForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_details
        fields =[
            'name',
            'phone_number',
            'message',
                ]
