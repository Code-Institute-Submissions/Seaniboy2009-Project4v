from .models import Booking, Table
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('table',)


class CreateTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_number', 'num_seats')
