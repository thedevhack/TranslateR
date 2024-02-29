from django.shortcuts import render
from api.utils import languages # noqa
from .models import UserIPList


def home(request):
    if request.method == "GET":
        visitors_count = UserIPList.objects.count()
        context = {'languages': languages, 'visitors_count': visitors_count}
        return render(request, 'main/home.html', context=context)
