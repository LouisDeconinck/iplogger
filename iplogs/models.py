from django.db import models

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(default="Unknown")
    referrer = models.TextField(default="Unknown")
    host = models.CharField(max_length=200, default="Unknown")
    path = models.CharField(max_length=200, default="Unknown")
    method = models.CharField(max_length=200, default="Unknown")
    cookies = models.TextField(default="Unknown")
    session_data = models.TextField(default="Unknown")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)