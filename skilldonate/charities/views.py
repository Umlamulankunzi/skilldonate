from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from .decorators import charity_required
from .models import SkillRequired
from volunteers.models import InterestInSkillRequired

# Create your views here.
def charities(request):
    return render(request, "charities/charity_index.html")


@login_required
@charity_required
def charity_home(request):
    skills = SkillRequired.objects.filter(charity=request.user.charity)
    context = {
        'skills': skills
    }
    # Grab user info from reqest obj
    return render(request, 'charities/charity_home.html', context)


@login_required
def skill_required_detail(request, skill_required_id):
    skill_required = SkillRequired.objects.get(id=skill_required_id)
    if skill_required.charity != request.user.charity:
        return redirect('charity-home')
    volunteer_interest = InterestInSkillRequired.objects.filter(skill_required=skill_required)
    context = {
        'skill_required': skill_required,
        'volunteers_interested': volunteer_interest
    }
    return render(request, 'charity/skill_required_detail.html', context)


@login_required
@charity_required
def create_skill_request(request):
    """Create a skill donation request"""
    #TODO: implement this
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.charity = request.user.charity
            question.save()
            return redirect('charity-home')
    else:
        form = QuestionForm()
    return render(request, 'app_auth/create_skill_request.html', {'form': form})
