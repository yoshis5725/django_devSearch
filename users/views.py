from django.shortcuts import render
from .models import Profile
from projects.models import Project


def profiles(request):
    all_profiles = Profile.objects.all()
    context = {'profiles': all_profiles}
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    skills_desc = profile.skill_set.exclude(description__exact='')  # filtering out skills w/o a description
    skills_no_desc = profile.skill_set.filter(description='')  # getting every skill with an empty description
    context = {'profile': profile, 'skills_desc': skills_desc, 'skills_no_desc': skills_no_desc}
    return render(request, 'users/user-profile.html', context)

