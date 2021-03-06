from cv import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from . import forms


def home(request):

    contact_form = forms.ContactForm()

    if request.method == 'POST':
        contact = forms.ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request, "Thanks for Contacting me")
            return redirect('cv:home')
        else:
            messages.error(request, "An error occurred")

    return render(request, "cv/home.html", {'contact_form': contact_form})
