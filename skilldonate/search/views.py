from django.shortcuts import render, redirect

# Create your views here.
def search_site(request):
    if request.method == "POST":
        # process search criteria
        return redirect("search")
    return render(request, 'search/search_site.html')
