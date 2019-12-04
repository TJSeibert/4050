from django.shortcuts import render, redirect
import random
from .forms import CheckoutForm
from django.forms.models import model_to_dict
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from cinema.models import Show, Promotion
import django

# Here's what's in a ticket object:
# * Show ID
# * Seat
# * Type

def total_price(cart):
    return sum(map(lambda t: 12, cart))


def cart(request):
    cart = request.session.get("cart", default=[])
    # In case the default was used
    request.session["cart"] = cart
    context = {'cart': get_disp_tickets(cart) }
    return render(request, "checkout/cart.html", context)


def get_disp_tickets(cart, promo=1):
    disp_tickets = []
    for ticket in cart:
        show = Show.objects.get(pk=ticket["show_id"])
        movie = show.movie_id
        disp_tickets.append({
            "name": movie.title,
            "type": ticket["type"],
            "seat": ticket["seat"],
            "time": show.scheduledTime,
            "price": 12 * promo
        })
    return disp_tickets


def display_form(request, form=None):
    cart = request.session["cart"]
    disp_tickets = get_disp_tickets(cart)
    # TODO :: Get ticket price from ticket.type
    context = { 'cart': disp_tickets, 'total_price': total_price(cart) }
    if form is None:
        profile = request.user.profile
        form = CheckoutForm({"billing_address": profile.billing_address, "expiration": profile.exp_date, "card_number": profile.card_number})
    context["form"] = form
    return render(request, "checkout/checkout.html", context)


def info(request):
    return display_form(request)


def finalize(request):
    cart = request.session["cart"]
    form = None
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            email_subject = "Confirm Your Purchase"
            user = request.user
            if form.fields["save"]:
                profile = user.profile
                fields = form.cleaned_data
                profile.exp_date = fields["expiration"]
                profile.billing_address = fields["billing_address"]
                profile.card_number = fields["card_number"]
                profile.card_type = fields["card_type"]
                profile.save()
            fields = form.cleaned_data
            promo_amt = 1
            now = django.utils.timezone.now()
            if fields["promo_code"]:
                for promotion in Promotion.objects.all():
                    if promotion.code == fields["promo_code"] and promotion.start <= now < promotion.end:
                        promo_amt = promotion.amt
            message = render_to_string("checkout/confirmation_email.html", context={"user": user, "cart": get_disp_tickets(cart, promo_amt)})
            print(message)
            to_email = user.email
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            messages.success(request, "Confirmation sent to email.")

            # TODO :: Put tickets in database

            del request.session["cart"]
            return redirect("cinema-home")
    return display_form(request, form)