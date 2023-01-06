from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .models import Review, Table, Booking
from .forms import BookingForm, CreateTableForm


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
                'booking_form': BookingForm(),
                'create_table_form': CreateTableForm(),
                'tables': tables,
                'bookings': bookings,
            },
        )

    def post(self, request, *args, **kwargs):
        tables = Table.objects.all()
        bookings = Booking.objects.all()

        booking_form = BookingForm(data=request.POST)

        if 'submit-booking' in request.POST:
            messages.info(request, 'Booking submitted')
            # bookingform = BookingForm(request.POST, prefix='banned')
            # if bookingform.is_valid():
            #     bookingform.save()
            # if booking_form.is_valid():
            #     booking_form.instance.table_number = request.user.email
            #     booking_form.instance.num_seats = request.user.username
            #     booking = booking_form.save(commit=False)
            #     booking.save()
            # else:
            #     booking_form = BookingForm()

        elif 'submit-new-table' in request.POST:
            messages.info(request, 'New table created')
            form = CreateTableForm(request.POST)

            if form.is_valid():
                messages.info(request, 'Form valid')

                table = form.save()
            # bookingform = BookingForm(request.POST, prefix='banned')
            # if bookingform.is_valid():
            #     bookingform.save()

        return render(
            request,
            "book.html",
            {
                'booking_form': BookingForm(),
                'create_table_form': CreateTableForm(),
                'tables': tables,
                'bookings': bookings,
            },
        )


class MenuPage(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "menu.html"
        )
