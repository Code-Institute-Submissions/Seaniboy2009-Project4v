from django.shortcuts import render, get_object_or_404
from django.views import generic, View


class HomePage(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "index.html"
        )
