from .models import Booking, Table, TIME_SLOTS, MenuItem
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
import datetime
from crispy_forms.helper import FormHelper


class CreateTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_number', 'num_seats')


class DeleteTableForm(forms.Form):
    table_number = forms.ModelChoiceField(queryset=Table.objects.all())
    fields = (table_number,)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        booking_time = forms.ChoiceField(choices=TIME_SLOTS,)
        first_name = forms.CharField(required=True)
        last_name = forms.CharField(required=True)
        email = forms.EmailField(required=True, max_length=100)
        fields = ('number_of_guests',
                  'booking_date',
                  'booking_time',
                  'first_name',
                  'last_name',
                  'email')
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
        fields = ('number_of_guests', 'booking_date', 'booking_time',)
        widgets = {
            'booking_date': forms.TextInput(attrs={'type': 'date'}),
        }


class CreateMenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('name', 'description', 'price', 'img', 'course')


class DeleteMenuItemForm(forms.Form):
    name = forms.ModelChoiceField(queryset=MenuItem.objects.all())
    fields = (name,)
