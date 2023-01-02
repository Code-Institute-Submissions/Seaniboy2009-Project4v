from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review, Table


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
        tables = Table.objects.all()

        return render(
            request,
            "book.html",
            {'tables': tables}
        )


class MenuPage(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "menu.html"
        )
