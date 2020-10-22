from django.shortcuts import render
from django import forms

from .models import Team


def index(request):
    form = forms.modelform_factory(Team, fields='__all__')

    return render(
        request, 'core/index.html', {'teams': Team.objects.all(), 'form': form}
    )
