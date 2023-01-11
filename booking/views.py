from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Review, Table, Booking, MenuItem, User
from .forms import BookingForm, CreateTableForm, DeleteTableForm
from django.views import generic, View
from django.contrib import messages


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
        tables = list(Table.objects.all())
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

        # bookingform = BookingForm(request.POST)

        def make_booking(table_to_book):
            """
            Update the booking form with the table and user, update the
            tables number of bookings
            """
            submited_booking.table = table_to_book
            submited_booking.booked_by = request.user
            submited_booking.save()
            table_to_book.update_num_of_bookings()
            table_to_book.save()
            messages.success(request, f'Thank you for making a booking with us, see you on {submited_booking.booking_date}')
            return HttpResponseRedirect(reverse("home"))

        def check_avalible_tables():
            """
            Check the list of all tables and look though each and see if they
            have a booking for the time and date, if they dontthey will be
            added to a list of avalible tables
            """
            list_of_tables = list(tables)
            booked_tables = []

            for booking in bookings:
                for table in list_of_tables:
                    if submited_booking.booking_date == booking.booking_date and submited_booking.booking_time == booking.booking_time and booking.table == table:
                        print(f'Booking Number: {booking.id}')
                        print(f'This table has the booking: {table.table_number}: Added to booked tables')
                        print('___________________________________________________')
                        booked_tables.append(table)
                    else:
                        print(f'Booking Number: {booking.id}')
                        print(f'This table does not have the booking: {table.table_number} Added to avalible tables')
                        print('___________________________________________________')

            list_of_tables.sort(key=lambda x: x.table_number)
            booked_tables.sort(key=lambda x: x.table_number)
            print('___________________________________________________')
            print(list_of_tables)
            print(booked_tables)
            print('___________________________________________________')
            if booked_tables == list_of_tables:
                messages.warning(request, 'Our apologies it looks like we are fully booked for this time and date')
                print('___________________________________________________')
            else:
                avalible_tables = []
                for table in list_of_tables:
                    if table not in booked_tables:
                        avalible_tables.append(table)
                print(f'Table {avalible_tables[0]} is avalble')
                return avalible_tables[0]

        if booking_form.is_valid():
            submited_booking = booking_form.save(commit=False)

            free_table = check_avalible_tables()
            if free_table:
                make_booking(free_table)

        else:
            booking_form = BookingForm()

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
        menu_items = MenuItem.objects.all()

        return render(
            request,
            "menu.html",
            {
                'menu_item': menu_items,
            }
        )


class managementPage(View):

    def get(self, request, *args, **kwargs):
        tables = list(Table.objects.all())
        bookings = Booking.objects.all()

        return render(
            request,
            "management.html",
            {
                'create_table_form': CreateTableForm(),
                'delete_table_form': DeleteTableForm(),
                'tables': tables,
                'bookings': bookings,
            },
        )

    def post(self, request, *args, **kwargs):
        tables = Table.objects.all()
        bookings = Booking.objects.all()

        if 'create-table' in request.POST:
            create_table = CreateTableForm(data=request.POST)
            print(f'Create table submitted')

            if create_table.is_valid():
                table = create_table.save()
                messages.success(request, 'New table created')

        if 'delete-table' in request.POST:
            delete_table = DeleteTableForm(data=request.POST)
            table = get_object_or_404(Table, table_number=request.POST['table_number'])
            print(table)
            table.delete()

        return render(
            request,
            "management.html",
            {
                'create_table_form': CreateTableForm(),
                'delete_table_form': DeleteTableForm(),
                'tables': tables,
                'bookings': bookings,
            },
        )
