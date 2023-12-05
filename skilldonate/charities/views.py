from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from app_auth.models import User, Volunteer, Charity
from .forms import ProfileUpdateForm, SkillRequiredForm
from .decorators import charity_required
from .models import SkillRequired, InterestInSkillDonated
from volunteers.models import InterestInSkillRequired, SkillDonated

# Create your views here.
def charities(request):
    return render(request, "charities/charity_index.html")



@login_required
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {'user': user}
    return render(request, "charities/charity_profile.html", context)


@login_required
@charity_required
def update_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    charity = Charity.objects.get(user=request.user)
    if request.method == "POST":
        # Update the profile and redirect to profile
        form = ProfileUpdateForm(request.POST, instance=charity)
        if form.is_valid():
            form.save()
            url = reverse('charity-profile', args=[user_id])
            return redirect(url)
    else:
        form = ProfileUpdateForm(instance=charity)
    return render(request, 'charities/update_profile.html', {'form': form})


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
def skills_required(request):
    skills = SkillRequired.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'charities/skills_required.html', context)


@login_required
def skill_required_detail(request, skill_required_id):
    skill_required = SkillRequired.objects.get(id=skill_required_id)
    # if skill_required.charity != request.user.charity:
    #     return redirect('charity-home')
    volunteer_interest = InterestInSkillRequired.objects.filter(skill_required=skill_required)
    context = {
        'skill_required': skill_required,
        'volunteers_interested': volunteer_interest
    }
    return render(request, 'charities/skill_required_detail.html', context)


@login_required
@charity_required
def create_skill_request(request):
    """Create a skill donation request"""
    #TODO: implement this
    if request.method == 'POST':
        form = SkillRequiredForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.charity = request.user.charity
            skill.save()
            return redirect('charity-home')
    else:
        form = SkillRequiredForm()
    return render(request, 'charities/create_skill_request.html', {'form': form})



@login_required
@charity_required
def show_interest_in_skill_donated(request, skill_donated_id):
    skill = SkillDonated.objects.get(id=skill_donated_id)

    if InterestInSkillDonted.objects.filter(
            skill_donated=skill, charity=request.user.charity).exists():
        # Change this to do nothing as interest already available
        # return redirect('charity-home')
        url = reverse('skill-donated-detail', args=[skill.id])
        return redirect(url)

    else:
        interest = InterestInSkillDonated()
        interest.charity = request.user.charity
        interest.skill_donated = skill
        interest.save()
        url = reverse('skill-donated-detail', args=[skill.id])
        return redirect(url)

    # TODO: Link this with a btton on the template page of list of skills
    # required
