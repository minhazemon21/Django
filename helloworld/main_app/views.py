from django.http import HttpResponse


def homeView(request):
    return HttpResponse("<h1>Maria Sultana Tuki</h1>")