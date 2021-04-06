from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    profiles = ["Mr. Krabs", "Reece", "John", "Jane" ]
    context = {
        'profiles': profiles,
    }
    return render(request, "home.html", context)


