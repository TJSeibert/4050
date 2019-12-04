from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from . models import Movie, Show, Showroom, seatInShowTime, Ticket
from . forms import TicketForm
from django.db.models import Q
from django.contrib import messages


def home(request):
    allmovies = Movie.objects.all()
    context = {
        'allmovies': allmovies
    }
    return render(request, 'cinema/home.html', context)


def browse(request):
    if request.GET:
        query = request.GET['q']
        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(title__icontains=query) | Q(category__icontains=query)
            results = Movie.objects.filter(lookups).distinct()
            context = {'results': results,
                       'submitbutton': submitbutton}
            return render(request, 'cinema/browse.html', context)

        else:
            return render(request, 'cinema/browse.html')
    else:
        return render(request, 'cinema/browse.html')


def render_ticket_form(request, form, context):
    context["form"] = form
    return render(request, 'cinema/ticketselection.html', context)


def ticketSelect(request):
    movies = Movie.objects.all()
    showrooms = Showroom.objects.all()
    shows = Show.objects.all()
    tickets = Ticket.objects.all()

    form = generate_form(4, 3, [], 0, 0, 0)

    context = {
        'movie': movies,
        'showroom': showrooms,
        'show': shows,
        'ticket': tickets
    }

    return render_ticket_form(request, form, context)


def generate_form(rows, cols, requested_seats, c_t, a_t, s_t):
    taken = []
    seats = []
    for x in range(cols):
        seats.append([])
        for y in range(rows):
            val = 0
            if (x, y) in requested_seats:
                val = 1
            if (x, y) in taken:
                val = -1
            seats[x].append(val)
    return TicketForm(c_t, a_t, s_t, seats)


def make_ticket(show, seat, ty):
    return {
        "show_id": show,
        "seat": seat,
        "type": ty
    }


def ticketCheck(request):
    import re
    seat_pattern = re.compile("^seat_([0-9]+)_([0-9]+)")

    # TODO :: Get this from the request
    show_id = 0

    cart = request.session.get("cart", default=[])
    if request.method == "POST":
        print(request.POST)
        valid = True
        seats = []
        for key, val in request.POST.items():
            match = seat_pattern.match(key)
            if match:
                x = int(match.group(1))
                y = int(match.group(2))
                seats.append((x, y))
                # TODO : Check whether seat taken
        child_tickets = int(request.POST["child_tickets"])
        adult_tickets = int(request.POST["adult_tickets"])
        senior_tickets = int(request.POST["senior_tickets"])

        ticket_amt = child_tickets + adult_tickets + senior_tickets
        if ticket_amt == 0:
            messages.error(request, "Must purchase at least 1 ticket.")
            valid = False
        elif len(seats) != ticket_amt:
            messages.error(request, f"Selected {len(seats)} seats for {ticket_amt} tickets.")
            valid = False

        if valid:
            for tick in range(child_tickets):
                cart.append(make_ticket(show_id, seats.pop(), "child"))
            for tick in range(adult_tickets):
                cart.append(make_ticket(show_id, seats.pop(), "adult"))
            for tick in range(senior_tickets):
                cart.append(make_ticket(show_id, seats.pop(), "senior"))
            request.session["cart"] = cart
            messages.success(request, "Tickets added to cart.")
            return redirect("checkout-cart")
        else:
            context = {}
            form = generate_form(4, 3, seats, child_tickets, adult_tickets, senior_tickets)
            return render_ticket_form(request, form, context)

    return render(request, 'cinema/ticketselection.html')


class MovieDetailView(DetailView):
    model = Movie


class ShowtimesListView(ListView):
    model = Show
