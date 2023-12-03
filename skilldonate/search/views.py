from django.shortcuts import render, redirect
from .forms import SearchForm
from volunteers.models import SkillRequired, Volunteer
from charities.models import Charity


# Create your views here.
# def search_site(request):
#     if request.method == "POST":
#         form = SearchForm(request.POST)
#         return redirect("search")
#     return render(request, 'search/search_site.html')


def search(request):
    CHOICES_MAP = {
        '1':'Donated Skill', '2': SkillRequired,
        '3': Charity, '4': Volunteer
    }
    if request.method == 'POST':
        # process contact info with provided email and message
        form = SearchForm(request.POST)
    else:
        form = SearchForm()

    if form.is_valid():
        # Access cleaned form data here
        category = form.cleaned_data['category']
        query = form.cleaned_data['query']
        search_results = None
        if category == '1':
            pass
        elif category == '2':
            search_results = SkillRequired.objects.filter(skill_name__icontains=query)
        elif category == '3':
            search_results = Charity.objects.filter(name__icontains=query)
        elif category == '4':
            search_results = Volunteer.objects.filter(name=query)

        context = {
            'category': category,
            'results': search_results,
        }
        return render(request, "search/search_results.html", context)

    return render(request, "search/search.html", {'form': form})
