from django.utils.deprecation import MiddlewareMixin
from main.models import UserIPList # noqa


class VisitorCountMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip_address = request.META.get('HTTP_X_REAL_IP')
        if ip_address:
            UserIPList.objects.get_or_create(ip_address=ip_address)
