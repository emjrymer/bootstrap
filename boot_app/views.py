from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from boot_app.models import Puppy


def index_view(request):
    return render_to_response('index.html', {})


def about_view(request):
    return render_to_response('aboutMe.html', {})


def info_view(request):
    all_puppy = Puppy.objects.all()
    return render_to_response('detailedinfo.html', {'puppies': all_puppy})


def application_view(request):
    return render_to_response('application_form.html', {})
