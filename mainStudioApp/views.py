import logging
logger = logging.getLogger('server_logger')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('server.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

import http

from django.shortcuts import render
from django.http import JsonResponse
from .models import FormRequests
import json

from . import bot
import asyncio

from urllib.parse import unquote

from .models import BotTrustedUsers

from django.views.decorators.csrf import csrf_exempt

# import logging
# logging.basicConfig(filename='error.log', encoding='utf-8', level=logging.DEBUG)

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

@csrf_exempt
def get_form(request, name, phone, email):
    try:
        name = unquote(name)
        email = unquote(email)
        # data = json.loads(request.body)
        # Get values from post
        logger.info(f'got data from front name {name}, phone {phone}, email {email}')
        # Save values into bd
        new_request = FormRequests.objects.create(name=name, phone=phone, email=email)
        new_request.save()
        logger.info('saved to db')
        for user in BotTrustedUsers.objects.all():
            print(f'sent to {user.user_id}')
            asyncio.run(bot.send(chat=user.user_id, msg=f'Получена заявка № {new_request.id}\nОт: {new_request.name}\nТелефон: {new_request.phone}\nEmail: {new_request.email}\nДата: {new_request.date}'))
            logger.info(f'sent to user {user.user_id}')

        return JsonResponse('Request received and saved', safe=False, status=http.HTTPStatus.OK)
    except:
        logger.info('error in form or bot')
        return JsonResponse('Empty form', safe=False)

def error_404(request, exception=None):
    return render(request, 'error_404.html', status=404)

@csrf_exempt
def registration_telegram(request, user_name, user_id):
    user, created = BotTrustedUsers.objects.get_or_create(name=user_name, user_id = user_id)
    user.save()
    return JsonResponse('Registered', status=http.HTTPStatus.OK, safe=False)
