from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('created_on',)
    list_display = ('title', 'slug', 'content', 'stars', 'created_on', 'status')
    search_fields = ['title', 'content']
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(status=1)
