from functools import wraps
from django.core.cache import cache
from django.http import HttpResponseForbidden
from api.models import APIMembership # noqa


def user_rate_limit(view_func):
    @wraps(view_func)
    def _wrapper_view(self, request, *args, **kwargs):
        user = request.user
        ip_address = request.META.get('REMOTE_ADDR')

        if user.is_authenticated:
            try:
                api_membership = APIMembership.objects.get(owner=user)
            except:
                api_membership = APIMembership.objects.create(owner=user)

            user_id = user.id

            request_count = cache.get(f"user_{user_id}")

            if request_count is None:
                request_count = 1
            else:
                request_count += 1

            cache.set(f"user_{user_id}", request_count, timeout=60)  # Adjust timeout as needed

            print("Request Count: ", request_count)

            if request_count > api_membership.tokens:
                return HttpResponseForbidden("Rate limit exceeded for this user.")

            return view_func(self, request, *args, **kwargs)

        else:

            request_count = cache.get(f"user_{ip_address}")

            if request_count is None:
                request_count = 1
            else:
                request_count += 1

            cache.set(f"user_{ip_address}", request_count, timeout=60)

            print("Request Count Anonymous: ", request_count)

            if request_count > 5:
                return HttpResponseForbidden("Rate limit exceeded for this Anonymous user.")

            return view_func(self, request, *args, **kwargs)

    return _wrapper_view
