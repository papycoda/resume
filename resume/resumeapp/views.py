from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    #basic template for the landing page
    return render(request, 'index.html')
