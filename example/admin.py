from django.contrib import admin

from .models import Sender
from .models import Message

admin.site.register(Sender)
admin.site.register(Message)
