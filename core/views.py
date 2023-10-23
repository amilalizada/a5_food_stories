from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    data = [1,2,34]
    context = {
        'data': data,
        'text': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos.',
        'name': 'John Doe',
    }
    return render(request, 'index.html', context=context)

def contact(request):  

    return render(request, 'contact.html')
