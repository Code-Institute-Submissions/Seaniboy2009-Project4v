from .models import Booking, Table
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('table', 'number_of_guests', 'booking_time', 'booked_by')
        widgets = {
            'booking_time': forms.TextInput(attrs={'type': 'date'}),
        }


class CreateTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_number', 'num_seats')


class DeleteTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_number',)
