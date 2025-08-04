# communications/views.py

from datetime import timedelta
from django.utils import timezone
from .models import CommunicationRecord
from django.shortcuts import render

def recent_interactions(request):
    thirty_days_ago = timezone.now() - timedelta(days=30)
    recent_records = CommunicationRecord.objects.filter(timestamp__gte=thirty_days_ago).order_by('-timestamp')
    
    context = {
        'recent_records': recent_records,
    }
    return render(request, 'communications/recent_interactions.html', context)

def customer_history(request, customer_name):
    customer_records = CommunicationRecord.objects.filter(customer_name=customer_name).order_by('-timestamp')
    
    context = {
        'customer_name': customer_name,
        'customer_records': customer_records,
    }
    return render(request, 'communications/customer_history.html', context)