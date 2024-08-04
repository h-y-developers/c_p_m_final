# from django.shortcuts import render,HttpResponse,redirect
# from .models import Admin,Achievements,Assignments,Assign_record,College,Comapnies,Department,Faculties,Projects,students,Subjects,Timetable,User_info
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView,View
from datetime import date
from ..filters import AchievementFilter
# from ..serialize import StudentSerialize
# from rest_framework.response import Response
# from rest_framework.decorators import api_view


# from ..decorators import students_required
from ..models import  Student, Events,Achievement,Exams,Project, User,Marks,Skills,Skill_list,Like
from ..forms import DocumentForm


def shome(request):
    return redirect('/students/login')
def StudentLoginView(request):
    if request.user.is_authenticated and user.is_student:
        userr = User.objects.get(username = request.user.username)
        url = '/students/profile/'+userr.slug
        return redirect(url)
    else:
        if request.method == 'POST':
            username = request.POST.get('susername')
            password =request.POST.get('spassword')
            if username == "" or password == "":
                messages.error(request,"Please fill all the fields")
                return redirect('/students/login')
            else:    
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_student:
                        login(request, user)
                        url = '/students/profile/'+user.slug
                        return redirect(url)
                    else:
                        messages.error(request, 'You are not authorized as students')   
                else:
                    messages.error(request, 'Username Or Password is incorrect')
                    return redirect('/students/login')
            
        context = {}
        return render(request, 'students/login.html', context)


def StudentLogoutView(request):
    return redirect('/logout')

def StudentForgetPassView(request):
    return redirect('/forgetPassword')


def StudentDashboardView(request):
    if request.user.is_authenticated and request.user.is_student:
        us = User.objects.get(username = request.user.username)
        try:
            usee = Student.objects.get(Id_number = request.user.username)
        except:
            usee = None
        achievements = Achievement.objects.filter(student_name=request.user.username)
        project = Project.objects.filter(student_name = request.user.username)
        if usee is not None:
            context={
            'student':usee,
            'achievements' : achievements,
            'projects': project
            }
            return render(request,"students/index.html",context)
        else:
            messages.error(request,'Please Fill the profile details first')
            url = '/students/profile/'+us.slug
            return redirect(url)
            
    else:
        return redirect('students/login')




def StudentEventView(request):
    if request.user.is_authenticated and request.user.is_student:
        userr = Events.objects.all()
        context = {
            'events':userr
        }
        return render(request,"students/events_see.html",context)
    else:
        return redirect('students/login')
# def StudentCertificateadd(request):
#     if request.user.is_authenticated and request.user.is_student:
#         return render(request,"students/certificate.html")
#     else:
#         return redirect('students/login')

def StudentCertificateView(request):
    if request.user.is_authenticated and request.user.is_student:
        if request.method == "POST" and 'certi' in request.FILES:
            certificate_name = request.POST.get('name')
            issuer_name = request.POST.get('company')
            field = request.POST.get('field')
            certificate_img = request.FILES['certi']
            form = Achievement(student_name= request.user.username,certificate_name=certificate_name,issuer_name=issuer_name,field_type = field,certificate_img=certificate_img)
            # form = Achievements(request.POST,request.FILES)
            form.save()
            return redirect('/students/achievements')

        
        return render(request,"students/certificate.html")
        #     form = Achievement(certificate_name=certificate_name,issuer_name=issuer_name,certificate_img=certificate_img)
        #     # form = Achievements(request.POST,request.FILES)
        #     form.save()
        #     return redirect('/students/achievements')
        #     # return render(request,"students/achievements.html")
        # else:
        #     return render(request,"students/certificate.html")
    else:
        return redirect('students/login')

def StudentProjectadd(request):
    if request.user.is_authenticated and request.user.is_student:
        return render(request,"students/add_project.html")
    else:
        return redirect('students/login')

def StudentExamView(request):
    if request.user.is_authenticated and request.user.is_student:
        
        try:
            userr = Marks.objects.get(id_no = request.user.username)    
        except:               
            userr = None

        context = {
            'exam':userr
        }
        return render(request,"students/exams.html",context)
    else:
        return redirect('students/login')

def StudentAchievementView(request):
    if request.user.is_authenticated and request.user.is_student:
        achieve = Achievement.objects.filter(student_name = request.user.username)
        # achieve = Achievement.objects.all()
        # achieve_filter = AchievementFilter(request.GET,queryset = achieve)
        context = {
            'achievements':achieve
        }
        return render(request,"students/achievements.html",context)
    else:
        return redirect('students/login')    

def Studentproject(request):
    if request.user.is_authenticated and request.user.is_student:
        project = Project.objects.filter(student_name = request.user.username)
        context = {
            'projects':project
        }
        return render(request,"students/projects.html",context)
    else:
        return redirect('students/login')    


def skills(request):
    if request.user.is_authenticated and request.user.is_student:
        if request.method == "POST":
            skills = request.POST.get('sk')
            try:
                useee = Skills.objects.get(username=request.user.username)
                useee.skills =  skills
                useee.save()
                return redirect('/students/skills')
            except:

                # interest = request.POST.get('interest')
                form = Skills(username=request.user.username,skills=skills)
                form.save()
                messages.success(request,"Data added success")
                return redirect('/students/skills')
        else:
            skill =  Skill_list.objects.all()
            try:
                own_skill = Skills.objects.get(username = request.user.username)
                skill_li = own_skill.skills.split(',')
            except:
                own_skill = None
                skill_li = []
            return render(request,'students/skill.html',{'skills':skill,'own_skill':skill_li})
            messages.error(request,"Data not Added")
               
    else:
        return redirect('students/login')



def like_project(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            p_name = request.POST.get('pname')
            project = Project.objects.get(project_name=p_name)

            if user in project.likes.all():
                project.likes.remove(user)
            else:
                project.likes.add(user)
            
            like ,created  = Like.objects.get_or_create(user=user,project=project)

            if not created:
                if like.value == "Like":
                    like.value = "Unlike"
                else:
                    like.value = "Like"
            like.save()
        return redirect('/students/project_see')
    else:
        return redirect('students/login')

def StudentProjectsee(request):
    if request.user.is_authenticated and request.user.is_student:
        project = Project.objects.all()
        context = {
            'projects':project
        }
        return render(request,"students/project_see.html",context)
    else:
        return redirect('students/login')

def StudentAddProjectView(request):
    if request.user.is_authenticated and request.user.is_student:
        if request.method == "POST":
            project_name = request.POST.get('name')
            description = request.POST.get('desc')
            url = request.POST.get('url')
            form = Project(student_name = request.user.username,project_name=project_name,description=description,url=url)
            form.save()
            return redirect('/students/projects')
            # return render(request,"students/projects.html")
        else:
            return render(request,"students/add_project.html")
    else:
        return redirect('students/login')




def delete_files(files_list):
    for file_ in files_list:
        if file_ and hasattr(file_, 'storage') and hasattr(file_, 'path'):
            # this accounts for different file storages (e.g. when using django-storages)
            storage_, path_ = file_.storage, file_.path
            storage_.delete(path_)



def StudentProfileSettingView(request,slug):
    if request.user.is_authenticated and request.user.is_student:
        userr = User.objects.get(slug = slug)
        stu = Student.objects.get(slug= slug)
        if request.method == "POST" and request.FILES['profile_pic']:
            profile_img = request.FILES['profile_pic']
            userr.profile_pic = profile_img
            stu.profile_pic = profile_img.name
            userr.save()
            stu.save()
            return redirect('/students/index')
        else:
            context ={
            'student':userr
            }
            return render(request,"students/edit_profile.html",context)

        
        
    else:
        return redirect('/students/login')  
# def studentsProfilesee(request):
#     if request.user.is_authenticated and request.user.is_student:

#         return render(request,"students/profile.html")
#     else:
#         return redirect('/login')
# def StudentProfileadd(request):
#     if request.user.is_authenticated and request.user.is_student:
#         return render(request,"students/profile.html")
#     else:
#         return redirect('students/login')

# <<<<<<< HEAD
# def decode_skill(skills):
#     """
#     Decode pizza pie toppings
#     """
#     skill = dict(Student.boolschoice)
#     decoded = [skill[t] for t in skills]
#     decoded.sort()
#     return ', '.join(decoded)





def StudentProfileUpdateView(request,slug):
    if request.method == "POST":
        # skills = request.POST.get('skills')
        # skil = dict(Student.boolschoice)
        # skill = [skil[t] for t in skills]
        
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
            # role = request.POST.get('role')

        dept = request.POST.get('dept')
        enrollment = request.POST.get('enrollment')
        permanent_address = request.POST.get('permanent_address')
        state = request.POST.get('state')
        resident_address = request.POST.get('resident_address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        country = request.POST.get('country')
        ssc = request.POST.get('ssc')
        ssc_res = request.POST.get('ssc_result')
        # ssc_path = request.POST.get('ssc_path')
        hsc = request.POST.get('hsc')
        hsc_res = request.POST.get('hsc_result')
        # hsc_path = request.POST.get('hsc_path')
        # skill = request.POST.get('skills')
        interest = request.POST.get('interest')
        website = request.POST.get('website')
        fb_link = request.POST.get('fb_link')
        linkedin_link = request.POST.get('linkedin_link')
        insta_link = request.POST.get('insta_link')
        id_noo = str(request.user.username)[:2]
        today_date = date.today()
        current = str(today_date.year)[2:4]
        id_year =  int(current) - int(id_noo)
        # if id_year == 1:
        #     id_year = r'1\u00bst'
        # elif id_year == 2:
        #     id_year = r'2\u00bnd'
        # elif id_year == 3:
        #     id_year = r'3\u00brd'
        # elif id_year == 4:
        #     id_year = r'4\u00bth'
        if id_year > 4:
            id_year = 'passout'

        
        try:
            
            userr = Student.objects.get(Id_number = request.user.username)
            userr.fname = fname
            userr.lname = lname
            userr.year = id_year
            userr.gender = gender
            userr.dob = dob
            userr.email = email
            userr.mobile = mobile
            userr.dept = dept
            userr.enrollment = enrollment
            
            userr.project = permanent_address
            userr.state = state
            userr.resident_address = resident_address
            userr.pincode = pincode
            userr.city = city
            userr.country = country
            userr.ssc = ssc
            userr.ssc_result = ssc_res
            
            userr.hsc = hsc
            userr.hsc_result = hsc_res
            # userr.hsc_path = hsc_path
            userr.website = website
            userr.fb_profile = fb_link
            userr.insta_profile = insta_link
            userr.linkedin_profile = linkedin_link
            # userr.skills.set(skill)
            # userr.interest = interest
            # for word in skill:
            #     userr.skills.add(word)
            userr.save()
            messages.success(request,"Updated")
            url = '/students/profile/'+str(slug)
            return redirect(url)


            
        except:
            form = Student.objects.create(Id_number= request.user.username,slug=slug,year=id_year,fname=fname,lname=lname,gender=gender,dob=dob,email=email,
            mobile=mobile,dept=dept,enrollment=enrollment,
            permanent_address=permanent_address,state=state,resident_address=resident_address,
            pincode=pincode,city=city,country=country,ssc=ssc,ssc_result=ssc_res,
            hsc=hsc,hsc_result=hsc_res,website=website,fb_profile=fb_link,insta_profile=insta_link,linkedin_profile=linkedin_link)
            # for word in skill:
            #     form.skills.add(word)
            # form.skills.set(skill)
            form.save()
            messages.success(request,"Inserted")

        
            url = '/students/profile/'+str(slug)
            return redirect(url)

    
    else:
        url = '/students/profile/'+str(slug)
        return redirect(url)
        



def StudentProfileView(request,slug):
    if request.user.is_authenticated and request.user.is_student:
        # if request.method == "POST" and 'ssc_result' in request.FILES or 'hsc_result' in request.FILES:

        #     fname = request.POST.get('fname')
        #     lname = request.POST.get('lname')
        #     gender = request.POST.get('gender')
        #     dob = request.POST.get('dob')
        #     email = request.POST.get('email')
        #     mobile = request.POST.get('mobile')
        #     # role = request.POST.get('role')
        #     dept = request.POST.get('dept')
        #     enrollment = request.POST.get('enrollment')
        #     id_no = request.POST.get('id_no')
        #     permanent_address = request.POST.get('permanent_address')
        #     state = request.POST.get('state')
        #     resident_address = request.POST.get('resident_address')
        #     pincode = request.POST.get('pincode')
        #     city = request.POST.get('city')
        #     country = request.POST.get('country')
        #     ssc = request.POST.get('ssc')
        #     ssc_res = request.FILES['ssc_result']
        #     hsc = request.POST.get('hsc')
        #     hsc_res = request.FILES['hsc_result']
        #     skills = request.POST.get('skills')
        #     interest = request.POST.get('interest')
            

        #     userr = User.objects.get(slug = slug)

        #     form = Student(Id_number= userr.username,slug = slug,fname=fname,lname=lname,gender=gender,dob=dob,email=email,
        #     mobile=mobile,dept=dept,enrollment=enrollment,id_no=id_no,
        #     permanent_address=permanent_address,state=state,resident_address=resident_address,
        #     pincode=pincode,city=city,country=country,ssc=ssc,ssc_result=ssc_res,
        #     hsc=hsc,hsc_result=hsc_res,skills=skills,interest=interest)
        #     form.save()
        #     url = '/students/profile/'+str(slug)
        #     return redirect(url)

        # else:
        try:
            userr = Student.objects.get(slug=slug)
        except:
            userr = None
        context={
                'student' : userr
        }
        return render(request,"students/profile.html",context)

        
        
        
    
          
    # else:
    #     return HttpResponse("<h1>not happening</h1>")
            

            # return redirect('/students/profile') 
            # return render(request,"students/index.html")

        
        # return render(request,"students/profile.html")
   
    else:
        return redirect('students/login')
     