from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from core.forms import ContactForm
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _
from .models import Contact
from .tasks import export

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
            return reverse_lazy('core:contact')
            
    elif request.method == "GET":
        form = ContactForm()
    context = {
        "form": form
    }
    return render(request, 'contact.html', context=context)

class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('core:contact')

    def form_valid(self, form):
        self.object = form.save()
        messages.add_message(self.request, messages.SUCCESS, _("Message sent successfully"))

        return super().form_valid(form)
    

def export_view(request):
    export.delay()
    return HttpResponse("Exporting")
