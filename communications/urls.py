# communications/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('recent/', views.recent_interactions, name='recent_interactions'),
    path('history/<str:customer_name>/', views.customer_history, name='customer_history'),
]