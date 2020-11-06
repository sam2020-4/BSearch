from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.conf import settings
from django.templatetags.static import static
from django.http import HttpResponse, Http404
import datetime as dt
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    date = dt.date.today() 

    all_countys = County.get_countys()
    
    if 'county' in request.GET and request.GET["county"]:
        countys = request.GET.get("county")
        searched_county = Donor.get_by_county(countys)       
        message = f"{countys}"
        all_countys = County.get_countys()        
        
        return render(request, 'index.html', {"message":message,"location": searched_county,
                                               "all_countys":all_countys})

    else:
        message = "No County Found!"

    return render(request, 'index.html', {"date": date, "all_countys":all_countys,})


# register method
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/accounts/login')
        
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {'form':form})


# search method for business    
@login_required(login_url='/accounts/login/')
def search_donors(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_projects = Donor.search_donor(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"donors": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

# get Donor by id method
def get_donor(request, id):

    try:
        project = Donor.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()    
    
    return render(request, "projects.html", {"project":project})
  
# new Donor method
@login_required(login_url='/accounts/login/')
def new_donor(request):
    current_user = request.user
    # profile = request.user.profile
    profile = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = NewDonorForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.Admin = current_user
            project.admin_profile = profile
            project.save()
        return redirect('index')

    else:
        form = NewDonorForm()
    return render(request, 'new-donor.html', {"form": form})

# user profiles method
@login_required(login_url='/accounts/login/')
def user_profiles(request):
    current_user = request.user
    profile = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        form2 = NewCountyForm(request.POST)
        
        if form2.is_valid():
            county = form2.save(commit=False)
            county.Admin = current_user
            county.admin_profile = profile
            county.save()
            return redirect('profile')
        
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')
            
    else:
        form = ProfileUpdateForm()
        form2 = NewCountyForm()

    return render(request, 'registration/profile.html', {"form":form, "form2":form2})



# def new_profile(request):
#     current_user = request.user

#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST,request.FILES)

#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.name = current_user
#             profile.save()

#         return redirect('profile')

#     else:
#         form= ProfileUpdateForm()

#     return render(request, 'registration/profile.html', {'form':form})


