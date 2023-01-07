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
            messages.info(request, 'Booking Form submitted')
            bookingform = BookingForm(request.POST)

            if bookingform.is_valid():
                booking = booking_form.save(commit=False)
                # commit=False tells Django that "Don't send this to database.
                table = tables[1]
                booking.table = table

                booking.save()
                messages.success(request, f'New Booking created and added to {table.table_number}')
            else:
                messages.warning(request, 'Form not')
                booking_form = BookingForm()

        elif 'submit-new-table' in request.POST:
            messages.info(request, 'New Table Form submitted')
            form = CreateTableForm(request.POST)

            if form.is_valid():
                table = form.save()
                messages.success(request, 'New table created')

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
