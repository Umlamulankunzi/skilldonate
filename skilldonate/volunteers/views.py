from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from app_auth.models import User
from app_auth.forms import VolunteerSignUpForm
from app_auth.decorators import volunteer_required
from charities.models import SkillRequired
from .models import InterestInSkillRequired, SkillOffered

# Create your views here.
def index(request):
    return render(request, "volunteers/volunteers_list.html")

@login_required
def profile(request, volunteer_id):
    user = get_object_or_404(User, id=volunteer_id)
    context = {'user': user}
    return render(request, "volunteers/volunteer_profile.html", context)

@login_required
@volunteer_required
def update_profile(request, volunteer_id):
    user = get_object_or_404(User, id=volunteer_id)
    if request.method == "POST":
        # Update the profile and redirect to profile
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            url = reverse('volunteer-profile', args=[volunteer_id])
            return redirect(url)
    else:
        form = VolunteerSignUpForm(instance=user)
    return render(request, 'volunteers/update_profile.html', {'form': form})



@login_required
@volunteer_required
def volunteer_home(request):
    """View that creates volunteer dashboard"""
    # !TODO: implement this feature

    # Getting only the 3 latest skills offered, volunteer should
    # importance given to required skills wjich volunteer should
    # be shown as much of.
    skills_offered = SkillOffered.objects.filter(
        volunteer=request.user.volunteer).order_by('-created_at')[:3]

    skills_required = SkillRequired.objects.all()
    context = {
        'skills_offered': skills_offered,
        'skills_required': skills_required
    }
    return render(request, 'volunteers/volunteer_home.html', context)



# SHOW THiS on
@login_required
@volunteer_required
def show_interest_in_skill_required(request, skill_required_id):
    skill = SkillRequired.objects.get(id=skill_required_id)

    if InterestInSkillRequired.objects.filter(
            skill_required=skill, volunteer=request.user.volunteer).exists():
        # Change this to do nothing as interest already available
        # return redirect('volunteer-home')
        url = reverse('skill-required-detail', args=[skill.id])
        return redirect(url)

    else:
        interest = InterestInSkillRequired()
        interest.volunteer = request.user.volunteer
        interest.skill_required = skill
        interest.save()
        url = reverse('skill-required-detail', args=[skill.id])
        return redirect(url)

    # TODO: Link this with a btton on the template page of list of skills
    # required
