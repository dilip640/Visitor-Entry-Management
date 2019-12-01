from django import forms
from entryapp.models import Visitor, Host
from phonenumber_field.formfields import PhoneNumberField

class CheckInForm(forms.ModelForm):

    class Meta:
        model= Visitor
        fields=["name", "email", "phone_number"]

class HostForm(forms.ModelForm):

    class Meta:
        model= Host
        fields=["name", "email", "phone_number"]

class CheckOutForm(forms.Form):
    phone = PhoneNumberField(region='IN')