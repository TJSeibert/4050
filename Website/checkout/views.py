from django.shortcuts import render

# Here's what's in a ticket object:
# * Movie ID
# * Showing ID
# * Seats
# * Type

def cart(request):
    cart = request.session["cart"]
    context = {}
    return render(request, "checkout/cart.html", context)