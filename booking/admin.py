from django.contrib import admin
from .models import Review, Table, Booking


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_filter = ('created_on',)
    list_display = ('id', 'title', 'slug', 'content', 'stars', 'created_on', 'status')
    search_fields = ['title', 'content']
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(status=1)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):

    list_filter = ('created_on',)
    list_display = ('id', 'table_number', 'created_on', 'has_booking')
    search_fields = ['table_number', ]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('booked_by', 'table', 'booking_time', 'booking_date', 'booked_on', 'approved',)
