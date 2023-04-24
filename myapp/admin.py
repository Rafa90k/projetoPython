from django.contrib import admin
from .models import Timer, SavedTime

admin.site.register(Timer)
admin.site.register(SavedTime)