from django.shortcuts import render
from django.http import JsonResponse
from .models import FormRequests
from django.template import RequestContext
import json

def index(request):
    return render(request, 'index.html')

def home_decor(request):
    return render(request, 'home-decor.html')

def kitchen_decor(request):
    return render(request, 'kitchen-decor.html')

def shatters_gallery(request):
    return render(request, 'shatters-gallery.html')

def form(request):
    return render(request, 'form.html')

def get_form(request):
    try:
        data = json.loads(request.body)
        # Get values from post
        name = data['name']
        phone = data['phone']
        email = data['email']

        # Save values into bd
        new_request = FormRequests.objects.create(name=name, phone=phone, email=email)
        new_request.save()

        #TODO email heandler integration

        return JsonResponse('Request received and saved', safe=False)
    except:
        return JsonResponse('Empty form', safe=False)

def error_404(request, exception=None):
    return render(request, 'error_404.html', status=404)


def handler404(request, *args, **argv):
    return render(request, 'error_404.html', status=404)