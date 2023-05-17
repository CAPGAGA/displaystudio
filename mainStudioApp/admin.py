from django.contrib import admin
from .models import FormRequests, BotTrustedUsers
# Register your models here.

admin.site.register(FormRequests)
admin.site.register(BotTrustedUsers)