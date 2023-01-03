from .models import Booking
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('table',)
        # widgets = {
        #     'booking_time': forms.TextInput(attrs={'type': 'date'}),
        # }
