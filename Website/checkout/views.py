from django.shortcuts import render, redirect
import random
from .forms import CheckoutForm
from django.forms.models import model_to_dict
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages

# Here's what's in a ticket object:
# * Movie ID
# * Showing ID
# * Seats
# * Type
# * Movie Name (after processing by this view)

def ticket():
    return {
    "m_id": 0,
    "show_id": 0,
    "seats": [(2, 'A')],
    "type": "matinee",
    "name": None
    }


def cart(request):
    cart = request.session.get("cart", default=[ticket(), ticket()])
    # In case the default was used
    request.session["cart"] = cart
    for tick in cart:
        # TODO :: Get movie name from database using ticket.m_id
        tick["name"] = "Movie Name"
    context = {'cart': cart}
    return render(request, "checkout/cart.html", context)

def info(request):
    cart = request.session["cart"]
    # TODO :: Get ticket price from ticket.type
    # TODO :: Get previous billing data if stored
    context = { 'cart': cart, 'total_price': sum(map(lambda t: 12, cart)), 'form': CheckoutForm() }
    return render(request, "checkout/checkout.html", context)

def finalize(request):
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            email_subject = "Confirm Your Purchase"
            user = request.user
            message = render_to_string("checkout/confirmation_email.html", {"user": user})
            to_email = user.email
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            messages.success(request, "Confirmation sent to email.")
            return redirect("cinema-home")
    return render(request, "checkout/cart.html", context)