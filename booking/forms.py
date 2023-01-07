from .models import Booking, Table, TIME_SLOTS
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
import datetime


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        booking_time = forms.ChoiceField(choices=TIME_SLOTS,)
        fields = ('number_of_guests', 'booking_date', 'booking_time', 'booked_by')
        widgets = {
            'booking_date': forms.TextInput(attrs={'type': 'date'}),
        }


class CreateTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_number', 'num_seats')


class DeleteTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_number',)
