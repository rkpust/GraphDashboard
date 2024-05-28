from django.shortcuts import render
from django.conf import settings


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if maintenance mode is enabled
        if settings.MAINTENANCE_MODE and request.user.is_superuser and settings.MAINTENANCE_MODE_IGNORE_SUPERUSER:
            return self.get_response(request)
        elif settings.MAINTENANCE_MODE:
            return render(request, 'maintenance/maintenance.html')
        else:
            return self.get_response(request)