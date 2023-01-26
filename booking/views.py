from .forms import (BookingForm,
                    CreateTableForm,
                    DeleteTableForm,
                    DeleteBookingForm,
                    EditBookingForm,
                    CreateMenuItemForm,
                    DeleteMenuItemForm)
from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Review, Table, Booking, MenuItem, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages
import datetime

ADMIN_ALLOWED_OPERATIONS = ['create-table', 'delete_table',
                            'create-menu-item', 'delete-menu-item']


def is_user_allowed(user, operation_name):
    '''
    Check to confirm a user can access some functions like deleting a table
    '''
    if operation_name in ADMIN_ALLOWED_OPERATIONS:
        if user.is_staff:
            return True
        else:
            return False
    return False


def delete_booking_object(request, booking):
    '''
    Deletes the passed booking from the DB
    '''
    table = booking.table
    table.remove_num_of_bookings()
    table.save()
    booking.delete()


def check_if_booked_before(request, submited_booking):
    """
    Check if the requested booking is from the same person and the same time
    and date, if booked by the user then cant book
    """
    bookings = Booking.objects.all()

    booked_before = False
    for booking in bookings:
        if (booking.booked_by == submited_booking.booked_by and
           booking.booking_date == submited_booking.booking_date and
           booking.booking_time == submited_booking.booking_time):

            booked_before = True

    if booked_before:
        return True
    else:
        return False


def compare_dates(request, submited_booking):
    """
    Compare todays date to the submitted booking and if
    booking is less than todays date cant book, else
    you can book
    """
    # Get todays date and the selected booking date
    booking_date = str(submited_booking.booking_date)
    today_date = str(datetime.datetime.now().strftime("%Y-%m-%d"))

    # Compare booking date and todays date so bookings cant be
    # in the past
    if booking_date < today_date:
        messages.warning(request, 'Date is in the past')
        return False
    else:
        return True


def make_booking(request, table_to_book, submited_booking):
    """
    Update the booking form with the table and user then update
    the form and save.
    This will then make the new booking.
    this will also update the tables number of bookings
    """
    submited_booking.table = table_to_book
    # the admin account is needed for users who did not
    # login
    user_admin = User.objects.get(username='admin')

    if request.user.is_authenticated:
        submited_booking.booked_by = request.user
    else:
        submited_booking.booked_by = user_admin

    submited_booking.save()
    table_to_book.add_num_of_bookings()
    table_to_book.save()


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

    # If this is already an existing booking try and get the object
    if edit:
        booking_to_edit = get_object_or_404(Booking, id=request.POST['id'])
        table = booking_to_edit.table
        table.remove_num_of_bookings()
        table.save()

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

    # Sort the lists so they can be compared correctly
    list_of_tables.sort(key=lambda x: x.table_number)
    booked_tables.sort(key=lambda x: x.table_number)
    if booked_tables == list_of_tables:
        messages.warning(request,
                         'Our apologies it looks like we are fully '
                         'booked for this time and date')

    else:
        # Check the size of avalible tables and the booking party size
        available_tables = []
        for table in list_of_tables:
            if table not in booked_tables:
                if check_table_size(table, submited_booking):
                    available_tables.append(table)

        # if there are tables avalible we can update a booking or
        # return the first avalible table
        if available_tables:
            if edit:
                table = available_tables[0]
                table.add_num_of_bookings()
                booking_to_edit.table = table
                booking_to_edit.booking_date = submited_booking.booking_date
                booking_to_edit.booking_time = submited_booking.booking_time
                booking_to_edit.save()
                messages.info(request, 'Booking updated '
                              f'{submited_booking.booking_date}')

            else:
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
                'edit_booking_form': EditBookingForm(),
                'bookings': bookings,
            },
        )

    def post(self, request, *args, **kwargs):
        tables = Table.objects.all()
        bookings = Booking.objects.all()

        if 'submit-booking' in request.POST:
            booking_form = BookingForm(data=request.POST)
            booking_form.booked_by = request.user.id

            if booking_form.is_valid():
                submited_booking = booking_form.save(commit=False)

                if compare_dates(request, submited_booking):
                    if check_if_booked_before(request, submited_booking):
                        messages.info(request, 'You have already made a '
                                               'booking with us')

                    else:
                        free_table = check_available_tables(submited_booking,
                                                            request, False)
                        if free_table:
                            make_booking(request, free_table, submited_booking)
                            messages.success(request, 'Thank you for making a booking with us, '
                                             f'see you on {submited_booking.booking_date}')

        elif 'delete-booking' in request.POST:
            delete_booking = DeleteBookingForm(data=request.POST)

            if delete_booking.is_valid():
                booking = get_object_or_404(Booking, id=request.POST['id'])
                delete_booking_object(request, booking)
                messages.warning(request, 'Booking has been deleted')

        elif 'edit-booking' in request.POST:
            edit_booking = EditBookingForm(data=request.POST)
            submited_booking = edit_booking.save(commit=False)

            booking_to_delete = get_object_or_404(Booking, id=request.POST['id'])
            submited_booking.booked_by = booking_to_delete.booked_by

            if compare_dates(request, submited_booking):
                if not check_if_booked_before(request, submited_booking):
                    free_table = check_available_tables(submited_booking,
                                                        request, False)
                    if free_table:
                        make_booking(request, free_table, submited_booking)
                        delete_booking_object(request, booking_to_delete)
                        messages.info(request, 'Booking updated '
                                      f'{submited_booking.booking_date}')
                else:
                    messages.warning(request, 'Already booked')

        else:
            booking_form = BookingForm()

        return render(
            request,
            "book.html",
            {
                'booking_form': BookingForm(),
                'create_table_form': CreateTableForm(),
                'delete_booking_form': DeleteBookingForm(),
                'edit_booking_form': EditBookingForm(),
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

        if ('create-table' in request.POST
           and is_user_allowed(request.user, 'create-table')):
            create_table = CreateTableForm(data=request.POST)

            if create_table.is_valid():
                table = create_table.save()
                messages.success(request, 'New table created')
            else:
                messages.warning(request,
                                 'Table with that name/number already exists')

        elif ('delete-table' in request.POST
              and is_user_allowed(request.user, 'create-table')):
            delete_table = DeleteTableForm(data=request.POST)
            table = get_object_or_404(Table,
                                      id=request.POST
                                      ['table_number'])

            if table:
                table.delete()
                messages.warning(request, f'{table} deleted')

            else:
                messages.info(request, 'table does not exist')

        elif 'delete-booking' in request.POST:
            delete_booking = DeleteBookingForm(data=request.POST)

            if delete_booking.is_valid():
                booking = get_object_or_404(Booking, id=request.POST['id'])
                delete_booking_object(request, booking)
                messages.warning(request, 'Booking has been deleted')

        elif ('create-menu-item' in request.POST
              and is_user_allowed(request.user, 'create-table')):
            create_menu_item = CreateMenuItemForm(request.POST, request.FILES)

            if create_menu_item.is_valid():
                create_menu_item.save()
                messages.success(request, 'New menu item created')
            else:
                messages.warning(request, 'Form invalid')

        elif ('delete-menu-item' in request.POST
              and is_user_allowed(request.user, 'create-table')):
            delete_menu_item = DeleteMenuItemForm(data=request.POST)
            menuItem = get_object_or_404(MenuItem, id=request.POST['name'])

            if delete_menu_item.is_valid():
                menuItem.delete()
                messages.warning(request, 'Item was deleted')
            else:
                messages.warning(request, 'Form invalid')

        elif 'edit-booking' in request.POST:
            edit_booking = EditBookingForm(data=request.POST)
            submited_booking = edit_booking.save(commit=False)

            booking_to_delete = get_object_or_404(Booking, id=request.POST['id'])
            submited_booking.booked_by = booking_to_delete.booked_by

            if compare_dates(request, submited_booking):
                if not check_if_booked_before(request, submited_booking):
                    free_table = check_available_tables(submited_booking,
                                                        request, False)
                    if free_table:
                        make_booking(request, free_table, submited_booking)
                        delete_booking_object(request, booking_to_delete)
                        messages.info(request, 'Booking updated '
                                      f'{submited_booking.booking_date}')
                else:
                    messages.warning(request, 'Already booked')
        else:
            return render(request, 'notallowed.html')

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
