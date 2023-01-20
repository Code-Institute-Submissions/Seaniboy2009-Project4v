from .forms import (BookingForm,
                    CreateTableForm,
                    DeleteTableForm,
                    DeleteBookingForm,
                    EditBookingForm,
                    CreateMenuItemForm,
                    DeleteMenuItemForm)
from django.shortcuts import render, get_object_or_404, reverse
from .models import Review, Table, Booking, MenuItem, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages


def check_table_size(table, booking):
    """
    Check the booking party size and compare to the table max size
    """
    seats = int(table.num_seats)
    request_seats = int(booking.number_of_guests)

    if seats >= request_seats:
        return True
    else:
        return False


def check_available_tables(submited_booking, request, edit):
    """
    Check the list of all tables and look though each and see if they
    have a booking for the time and date of the submited_booking,
    if they dont they will be added to a list of available tables
    """
    tables = Table.objects.all()
    bookings = Booking.objects.all()
    if edit:
        booking_to_edit = get_object_or_404(Booking, id=request.POST['id'])
        print(booking_to_edit)
    list_of_tables = list(tables)
    booked_tables = []

    # Goes over each booking and its assigned table and sees if it has the
    # booking if the table does not have the booking it can be used
    for booking in bookings:
        for table in list_of_tables:
            if (submited_booking.booking_date == booking.booking_date
               and submited_booking.booking_time == booking.booking_time
               and booking.table == table):
                booked_tables.append(table)

    list_of_tables.sort(key=lambda x: x.table_number)
    booked_tables.sort(key=lambda x: x.table_number)
    if booked_tables == list_of_tables:
        messages.warning(request,
                         'Our apologies it looks like we are fully'
                         'booked for this time and date')

    else:
        available_tables = []
        for table in list_of_tables:
            if table not in booked_tables:
                if check_table_size(table, submited_booking):
                    available_tables.append(table)

        # checks if its an edidted booking or new booking
        if available_tables:
            if edit:
                print('Edit')
                table = available_tables[0]
                booking_to_edit.table = table
                booking_to_edit.booking_date = submited_booking.booking_date
                booking_to_edit.booking_time = submited_booking.booking_time
                booking_to_edit.save()
                print(f'Edited {booking_to_edit}')
                messages.info(request, 'Booking updated'
                              f'{submited_booking.booking_date}')

            else:
                print('Not edit')
                return available_tables[0]
        else:
            messages.warning(request, 'Our apologies it looks like we have no '
                             'free tables for your party size')


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
                'delete_booking_form': DeleteBookingForm(),
                'tables': tables,
                'bookings': bookings,
            },
        )

    def post(self, request, *args, **kwargs):
        tables = Table.objects.all()
        bookings = Booking.objects.all()
        user_admin = User.objects.get(username='admin')
        booking_form = BookingForm(data=request.POST)

        def make_booking(table_to_book):
            """
            Update the booking form with the table and user then update
            the form and save this will then make the new booking.
            this will also update the tables number of bookings
            """
            submited_booking.table = table_to_book

            if request.user.is_authenticated:
                submited_booking.booked_by = request.user
            else:
                submited_booking.booked_by = user_admin

            submited_booking.save()
            table_to_book.add_num_of_bookings()
            table_to_book.save()
            messages.success(request, 'Thank you for making a booking with us,'
                             f'see you on {submited_booking.booking_date}')

        if booking_form.is_valid():
            submited_booking = booking_form.save(commit=False)

            # check if user has booked before and if its for the same date/time
            has_booked = False
            if bookings:
                for booking in bookings:
                    if (booking.first_name == submited_booking.first_name
                       and booking.last_name == submited_booking.last_name
                       and booking.booking_date == submited_booking.booking_date
                       and booking.booking_time == submited_booking.booking_time):

                        has_booked = True
                        break

            if has_booked:
                messages.info(request, 'You have already made a'
                                       'booking with us')
            else:
                free_table = check_available_tables(submited_booking,
                                                    request, False)
                if free_table:
                    make_booking(free_table)

        elif 'delete-booking' in request.POST:
            print('delete-booking')
            delete_booking = DeleteBookingForm(data=request.POST)
            print(delete_booking)

            if delete_booking.is_valid():
                print("delete-booking Form is valid")
                booking = get_object_or_404(Booking, id=request.POST['id'])
                table = booking.table
                table.remove_num_of_bookings()
                table.save()
                booking.delete()

        else:
            booking_form = BookingForm()

        return render(
            request,
            "book.html",
            {
                'booking_form': BookingForm(),
                'create_table_form': CreateTableForm(),
                'delete_booking_form': DeleteBookingForm(),
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


class ManagementPage(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        tables = Table.objects.all()
        bookings = Booking.objects.all()

        return render(
            request,
            "management.html",
            {
                'create_table_form': CreateTableForm(),
                'delete_table_form': DeleteTableForm(),
                'delete_booking_form': DeleteBookingForm(),
                'edit_booking_form': EditBookingForm(),
                'create_menu_item_form': CreateMenuItemForm(),
                'delete_menu_item_form': DeleteMenuItemForm(),
                'tables': tables,
                'bookings': bookings,
            },
        )

    def post(self, request, *args, **kwargs):
        tables = Table.objects.all()
        bookings = Booking.objects.all()
        print('Form submitted')
        print(request.POST)

        if 'create-table' in request.POST:
            print('create-table')
            create_table = CreateTableForm(data=request.POST)
            print(create_table)

            if create_table.is_valid():
                table = create_table.save()
                messages.success(request, 'New table created')
            else:
                messages.warning(request,
                                 'Table with that name/number already exists')

        elif 'delete-table' in request.POST:
            print('delete-table')
            delete_table = DeleteTableForm(data=request.POST)
            print(delete_table)
            table = get_object_or_404(Table,
                                      id=request.POST
                                      ['table_number'])

            if table:
                print(table)
                table.delete()
                messages.success(request, f'{table} deleted')
            else:
                messages.warning(request, 'table does not exist')
                print('Does not exist')

        elif 'delete-booking' in request.POST:
            print('delete-booking')
            delete_booking = DeleteBookingForm(data=request.POST)
            print(delete_booking)

            if delete_booking.is_valid():
                print("delete-booking Form is valid")
                booking = get_object_or_404(Booking, id=request.POST['id'])
                table = booking.table
                table.remove_num_of_bookings()
                table.save()
                booking.delete()

        elif 'create-menu-item' in request.POST:
            print('create-menu-item called')
            create_menu_item = CreateMenuItemForm(request.POST, request.FILES)

            if create_menu_item.is_valid():
                print('create-menu-item form is valid')
                create_menu_item.save()
                messages.success(request, 'New menu item created')

        elif 'delete-menu-item' in request.POST:
            print('delete-menu-item called')
            delete_menu_item = DeleteMenuItemForm(data=request.POST)
            print(request.POST['name'])
            menuItem = get_object_or_404(MenuItem, id=request.POST['name'])
            print(menuItem)

            if delete_menu_item.is_valid():
                print('create-menu-item form is valid')
                menuItem.delete()
                messages.success(request, 'Item was deleted')

        elif 'edit-booking' in request.POST:
            edit_booking = EditBookingForm(data=request.POST)
            print(edit_booking)
            submited_booking = edit_booking.save(commit=False)
            list(tables)
            list_of_tables = list(tables)
            booked_tables = []
            check_available_tables(submited_booking, request, True)

        return render(
            request,
            "management.html",
            {
                'create_table_form': CreateTableForm(),
                'delete_table_form': DeleteTableForm(),
                'delete_booking_form': DeleteBookingForm(),
                'edit_booking_form': EditBookingForm(),
                'create_menu_item_form': CreateMenuItemForm(),
                'delete_menu_item_form': DeleteMenuItemForm(),
                'tables': tables,
                'bookings': bookings,
            },
        )
