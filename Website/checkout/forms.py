from django import forms
from django.core.validators import RegexValidator


class CheckoutForm(forms.Form):
    billing_address = forms.CharField(label="Billing Address")
    card_type = forms.ChoiceField(choices=[("MC", "MasterCard"), ("VS", "Visa")])
    card_number = forms.RegexField(regex="\\d{16}", label="Card Number")
    expiration = forms.RegexField(regex="[01][1-9]/[0-9][0-9]", label="Expiration Date")
    promo_code = forms.CharField(required=False, label="Promo Code")
    save = forms.BooleanField(required=False, label="Save Payment Information")