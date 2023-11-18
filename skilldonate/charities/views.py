from django.shortcuts import render, HttpResponse

# Create your views here.
def charities(request):
    return render(request, "charities/charity_index.html")
