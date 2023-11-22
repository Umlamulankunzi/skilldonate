from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "homepage.html")

def how_it_works(request):
    return render(request, "how_it_works.html")

def contact(request):
    if request.method == 'POST':
        # process contact info with provided email and message
        return redirect("contact")
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
