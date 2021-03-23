from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView,View
from ..models import  Student, Events,Achievement,Exams,Project, User,Requirements
from ..forms import DocumentForm


def CompanyLoginView(request):
    if request.user.is_authenticated:
        return redirect('/company/index')
    else:
        if request.method == 'POST':
            username = request.POST.get('cusername')
            password =request.POST.get('cpassword')
            if username == "" or password == "":
                messages.error(request,"Please fill all the fields")
                return redirect('/company/login')
            else:    
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_company:
                        login(request, user)
                        return redirect('/company/index')
                    else:
                        messages.error(request, 'You are not authorized as Company')   
                else:
                    messages.error(request, 'Username Or Password is incorrect')
                    return redirect('/company/login')
            
        context = {}
        return render(request, 'company/login.html', context)


def CompanyLogoutView(request):
    return redirect('/logout')

def CompanyForgetPassView(request):
    return redirect('/forgetPassword')

def CompanyProfileSettingView(request,slug):
    if request.user.is_authenticated and request.user.is_company:
        userr = User.objects.get(slug = slug)
        if request.method == "POST" and request.FILES['profile_pic']:
            profile_img = request.FILES['profile_pic']
            userr.profile_pic = profile_img
            userr.save()
            
            return redirect('/company/index')
        else:
            context ={
            'company':userr
            }
            return render(request,"company/edit_profile.html",context)
    else:
        return redirect('/company/login')


def CompanyDashboardView(request):
    if request.user.is_authenticated and request.user.is_company:
        return render(request,"company/index.html")
    else:
        return redirect('/company/login')



def CompanyFindCandidate(request):
    if request.user.is_authenticated and request.user.is_company:
        return render(request,"company/find_candidate.html")
    else:
        return redirect('/company/login')


def CompanyRequirements(request):
    if request.user.is_authenticated and request.user.is_company:
        if request.method == "POST" and 'file' in request.FILES:
            company_name = request.POST.get('name')
            job_description = request.POST.get('desc')
            no_of_vacancies = request.POST.get('vacancies')
            url = request.POST.get('url')
            file = request.FILES['file']
            form = Requirements(company_name=company_name,job_description=job_description,no_of_vacancies=no_of_vacancies,url=url,file=file)
           
            form.save()
            messages.success(request," Uploaded")
        # return redirect('/company/requirements')
        return render(request,'company/requirements.html')
   
    else:
        return redirect('/company/login')
