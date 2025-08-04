# communications/admin.py

from django.contrib import admin
from .models import CommunicationRecord

admin.site.register(CommunicationRecord)