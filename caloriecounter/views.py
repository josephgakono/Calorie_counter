from django.http import HttpResponse


def home(request):
    return HttpResponse("Calorie counter is running.")
