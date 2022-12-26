from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review


class HomePage(View):

    def get(self, request, *args, **kwargs):
        # queryset = Review.objects.all()
        # reviews = get_object_or_404(queryset)
        reviews = Review.objects.all()

        return render(
            request,
            "index.html",
            {'review_list': reviews}
        )


class BookingPage(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "book.html"
        )


class MenuPage(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "menu.html"
        )
