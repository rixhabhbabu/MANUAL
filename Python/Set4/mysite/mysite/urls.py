from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")

def trigger_error(request):
    return HttpResponseServerError("Intentional Error for Debugging")

urlpatterns = [
    path('', home),  # Root URL
    path('error/', trigger_error),  # Error URL
]