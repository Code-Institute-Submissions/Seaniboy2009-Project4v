from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Table, Booking
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
            table = table_to_book
            submited_booking.table = table
            submited_booking.save()
            messages.success(request, f'Thank you for making a booking with us, see you on {booking.booking_date}')
            return HttpResponseRedirect(reverse("home"))

        def check_table(current_table, table_to_check):

            if current_table == table_to_check:
                return True
            else:
                return False

        # if the submitted form is the booking form
        if 'submit-booking' in request.POST:
            bookingform = BookingForm(request.POST)

            if bookingform.is_valid():
                # commit=False tells Django "Don't send this to database.
                submited_booking = booking_form.save(commit=False)
                # List of all avalible tables, updated if there is a post requestd
                list_of_tables = []
                # List of all tables that are booked for the date and time of the post request
                booked_tables = []

                for table in tables:
                    list_of_tables.append(table)

                # check each booking
                for booking in bookings:
                    print(f'Booking Number: {booking.id}')
                    # check what table has the booking
                    for table in list_of_tables:
                        print(f'Table: {table.table_number}')
                        # check if bookings has a booking for time and date, then check if its for the same table
                        if submited_booking.booking_date == booking.booking_date and submited_booking.booking_time == booking.booking_time and booking.table == table:
                            print(f'This table has the booking: {table.table_number}')
                            booked_tables.append(table)
                        else:
                            print(f'This table does not have the booking: {table.table_number}')

                list_of_tables.sort(key=lambda x: x.table_number)
                booked_tables.sort(key=lambda x: x.table_number)
                if booked_tables == list_of_tables:
                    messages.warning(request, 'No free tables for this date and time')
                else:
                    avalible_tables = []
                    for table in list_of_tables:
                        if table not in booked_tables:
                            avalible_tables.append(table)
                    make_booking(avalible_tables[0])

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
            item = get_object_or_404(Table, table_number=request.POST['table_number'])
            print(item)
            item.delete()

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
