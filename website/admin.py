from django.contrib import admin
from django.conf import settings

# Register your models here.

from .models import Logger

import os
from django.http import HttpResponse

# Register your models here.
def view_log_file(modeladmin, request, queryset):
    log_file_path = os.path.join(settings.BASE_DIR, 'logs/error.log')

    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            log_content = log_file.read()

        return HttpResponse(log_content, content_type='text/plain')

    return HttpResponse("Log file not found.", content_type='text/plain')

view_log_file.short_description = "View Log File"

@admin.register(Logger)
class ProfileAdmin(admin.ModelAdmin):
    actions = [view_log_file]# Register the custom action with the ProfileAdmin
