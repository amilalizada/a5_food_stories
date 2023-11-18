from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from core.forms import ContactForm

# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def contact(request):  
    form = None
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Message sent successfully")
            return redirect('contact')
            
    elif request.method == "GET":
        form = ContactForm()
    context = {
        "form": form
    }
    return render(request, 'contact.html', context=context)
