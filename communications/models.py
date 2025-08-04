from django.db import models

class CommunicationRecord(models.Model):
    CHANNEL_CHOICES = (
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('chat', 'Chat'),
        ('in_person', 'In Person'),
    )
    DIRECTION_CHOICES = (
        ('inbound', 'Inbound'),
        ('outbound', 'Outbound'),
    )

    customer_name = models.CharField(max_length=100)
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)
    summary = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Communication with {self.customer_name} via {self.channel} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
