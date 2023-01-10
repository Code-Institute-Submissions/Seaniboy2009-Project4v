from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Table, Booking, User
from .forms import BookingForm, CreateTableForm, DeleteTableForm


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

        def make_booking(table_to_book):
            """
            Update the booking form with the picked table and user who booked and submit to the DB
            """
            submited_booking.table = table_to_book
            submited_booking.booked_by = request.user
            submited_booking.save()
            messages.success(request, f'Thank you for making a booking with us, see you on {submited_booking.booking_date}')
            return HttpResponseRedirect(reverse("home"))

        def check_avalible_tables():
            """
            Check the list of all tables and look though each and see if they have a booking for the time and date, if they dont
            they will be added to a list of avalible tables
            """
            list_of_tables = list(tables)
            list_of_free_tables = []

            booked_tables = []
            for booking in bookings:
                print(f'Booking Number: {booking.id}')
                # check what table has the booking
                for table in list_of_tables:
                    print(f'Table: {table.table_number}')
                    # check if bookings has a booking for time and date, then check if its for the same table
                    if submited_booking.booking_date == booking.booking_date and submited_booking.booking_time == booking.booking_time and booking.table == table:
                        print(f'This table has the booking: {table.table_number}: Added to booked tables')
                        print('___________________________________________________')
                        booked_tables.append(table)
                    else:
                        print(f'This table does not have the booking: {table.table_number} Added to avalible tables')
                        print('___________________________________________________')
                        list_of_free_tables.append(table)

            list_of_free_tables.sort(key=lambda x: x.table_number)
            list_of_tables.sort(key=lambda x: x.table_number)
            booked_tables.sort(key=lambda x: x.table_number)
            print('___________________________________________________')
            print(list_of_free_tables)
            print(list_of_tables)
            print(booked_tables)
            print('___________________________________________________')
            if booked_tables == list_of_tables:
                messages.warning(request, 'No free tables for this date and time')
                print('___________________________________________________')
            else:
                avalible_tables = []
                for table in list_of_tables:
                    if table not in booked_tables:
                        avalible_tables.append(table)
                print(f'Table {avalible_tables[0]} is avalble')
                return avalible_tables[0]

        # if the submitted form is the booking form
        if 'submit-booking' in request.POST:
            bookingform = BookingForm(request.POST)

            if bookingform.is_valid():
                # commit=False tells Django "Don't send this to database.
                submited_booking = booking_form.save(commit=False)

                table = check_avalible_tables()

                if table:
                    make_booking(table)


                # list_of_tables = []
                # for table in tables:
                #     list_of_tables.append(table)

                # booked_tables = []
                # for booking in bookings:
                #     print(f'Booking Number: {booking.id}')
                #     # check what table has the booking
                #     for table in list_of_tables:
                #         print(f'Table: {table.table_number}')
                #         # check if bookings has a booking for time and date, then check if its for the same table
                #         if submited_booking.booking_date == booking.booking_date and submited_booking.booking_time == booking.booking_time and booking.table == table:
                #             print(f'This table has the booking: {table.table_number}')
                #             booked_tables.append(table)
                #         else:
                #             print(f'This table does not have the booking: {table.table_number}')

                # list_of_tables.sort(key=lambda x: x.table_number)
                # booked_tables.sort(key=lambda x: x.table_number)
                # if booked_tables == list_of_tables:
                #     messages.warning(request, 'No free tables for this date and time')
                # else:
                #     avalible_tables = []
                #     for table in list_of_tables:
                #         if table not in booked_tables:
                #             avalible_tables.append(table)
                #     make_booking(avalible_tables[0])

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

        return render(
            request,
            "menu.html"
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
