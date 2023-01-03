from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review, Table, Booking
from .forms import BookingForm


class HomePage(View):

    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all()

        return render(
            request,
            "index.html",
            {'review_list': reviews}
        )


class BookingPage(View):

    def get(self, request, *args, **kwargs):
        tables = Table.objects.all()
        bookings = Booking.objects.all()

        return render(
            request,
            "book.html",
            {
                "booking_form": BookingForm(),
                'tables': tables,
                'bookings': bookings,
            },
        )

    def post(self, request, *args, **kwargs):
        table = get_object_or_404(Table, id=id)


class MenuPage(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "menu.html"
        )
