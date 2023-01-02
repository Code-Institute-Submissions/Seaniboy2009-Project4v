from django.contrib import admin
from .models import Review, Table


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_filter = ('created_on',)
    list_display = ('title', 'slug', 'content', 'stars', 'created_on', 'status')
    search_fields = ['title', 'content']
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(status=1)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):

    list_filter = ('created_on',)
    list_display = ('table_number', 'name', 'created_on',)
    search_fields = ['table_number', ]
