from django import forms
from entryapp.models import Visitor, Host

class CheckInForm(forms.ModelForm):

    class Meta:
        model= Visitor
        fields=["name", "email", "phone_number"]

class HostForm(forms.ModelForm):

    class Meta:
        model= Host
        fields=["name", "email", "phone_number"]