from django import forms
from django.core.validators import RegexValidator


class CheckoutForm(forms.Form):
    billing_address = forms.CharField()
    card_type = forms.ChoiceField(choices=[("MC", "MasterCard"), ("VS", "Visa")])
    card_number = forms.RegexField(regex="\\d{16}")
    expiration = forms.RegexField(regex="[01][1-9]/[0-9][0-9]")
    promo_code = forms.CharField()
    save = forms.BooleanField()