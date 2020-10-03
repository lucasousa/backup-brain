from django.shortcuts import render
from django.views.generic import  CreateView
from .models import Wiki


class WikiCreate(CreateView):
    template_name = "wiki/create.html"
    model = Wiki
    fields = ['title', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wikis'] = Wiki.objects.all()
        return context
