from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the meeting planner!")


def date(request):
    return HttpResponse(f"Welcome to the meeting planner! the date is {datetime.now()}")


def about(request):
    return HttpResponse("This is the about page!")
