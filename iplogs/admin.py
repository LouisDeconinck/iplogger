from django.contrib import admin

from .models import IPAddress

class IPAddressAdmin(admin.ModelAdmin):
    fields = ['ip_address', 'user_agent', 'referrer', 'host', 'path', 'method', 'cookies', 'session_data', 'meta_request', 'latitude', 'longitude']
    list_display = ('ip_address', 'user_agent', 'referrer', 'host', 'path', 'method', 'cookies', 'session_data', 'meta_request', 'latitude', 'longitude', 'timestamp')
    readonly_fields = ('timestamp',)

admin.site.register(IPAddress, IPAddressAdmin)
