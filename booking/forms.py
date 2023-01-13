from .models import Booking, Table, TIME_SLOTS
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
import datetime


class CreateTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_number', 'num_seats')


class DeleteTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_number',)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        booking_time = forms.ChoiceField(choices=TIME_SLOTS,)
        fields = ('number_of_guests', 'booking_date', 'booking_time', 'first_name', 'last_name', 'email')
        widgets = {
            'booking_date': forms.TextInput(attrs={'type': 'date'}),
        }


class DeleteBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('id',)


class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        booking_time = forms.ChoiceField(choices=TIME_SLOTS,)
        number_of_guests = forms.ChoiceField(choices=NUMBER_OF_SEATS,)
        fields = ('number_of_guests', 'booking_date', 'booking_time',)
        widgets = {
            'booking_date': forms.TextInput(attrs={'type': 'date'}),
        }
