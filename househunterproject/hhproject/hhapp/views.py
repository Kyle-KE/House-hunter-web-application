from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import hostel
from .forms import HostelForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, 
                                DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

class CreateHostelView(CreateView):
    model = hostel
    form_class = HostelForm

class HostelListView(ListView):
    model = hostel

class HostelDetailView(DetailView):
    model = hostel


    def get_queryset(self):
        return hostel.objects.all()

def home(request):
    return render(request, 'hhapp/home.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('hhapp:home'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'hhapp/login.html', {})

def user_registration(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = user.objects.create_user(username=username, password=password, email=email)
        user.set_password(user.password)
        user=UserForm(request.POST, instance=user)
        user.save()
        return HttpResponseRedirect(reverse('hhapp:home'))
    else:
        return render(request, 'hhapp/registration.html', {'user_form': UserForm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('hhapp:home'))

# def user_registration(request):
#     registered = False
#     if request.method == "POST":
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileInfoForm(data=request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             if 'profile_pic' in request.FILES:
#                 profile.profile_pic = request.FILES['profile_pic']
#             profile.save()
#             registered = True
#         else:
#             print(user_form.errors, profile_form.errors)
        
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileInfoForm()
#     return render(request, 'basic_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})