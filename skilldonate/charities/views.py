from django.shortcuts import render, HttpResponse

# Create your views here.
def charities(request):
    return HttpResponse("<h1>CHARITIES</h1>")
