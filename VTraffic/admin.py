from django.contrib import admin
from .models import First_Page, Officer_Page, Ticket, Notification, Payment

admin.site.register(First_Page)
admin.site.register(Officer_Page)
admin.site.register(Ticket)
admin.site.register(Notification)
admin.site.register(Payment)