from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView,View
from ..models import  Student, Events,Achievement,Exams,Project, User,Requirements,Company,Marks, Skills, Skill_list
from ..forms import DocumentForm


def CompanyLoginView(request):
    if request.user.is_authenticated and request.user.is_company:
        userr = User.objects.get(username = request.user.username)
        url = '/company/profile/'+userr.slug
        return redirect(url)
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
                        url = '/company/profile/'+user.slug
                        return redirect(url)
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
        usee = Company.objects.get(company_username = request.user.username)
        # achievements = Achievement.objects.filter(student_name=request.user.username)
        # project = Project.objects.filter(student_name = request.user.username)
        context={
            'company':usee
            # 'achievements' : achievements,
            # 'projects': project
        }
        return render(request,"company/index.html",context)
    else:
        return redirect('/company/login')



def CompanyFindCandidateFilter(request):
    if request.user.is_authenticated and request.user.is_company:
        if request.method == "GET" and 'student_year' in request.GET:
            year_id = request.GET['student_year']
            dept = request.GET['achieve_type']
            if dept == 'All':
                if year_id is not None or year_id!='':
                    userr = Student.objects.filter(year = year_id)
                else:
                    userr = Student.objects.all()
                        
                
            else:
                if year_id is not None or year_id != '': 
                    userr = Student.objects.filter(dept = dept,year=year_id)

                else:
                    userr = Student.objects.filter(dept = dept)    
                
            
            
            
            context = {
                'students':userr,
                'dept' : dept
            }
            return render(request,"company/find_candidate.html",context)
        else:
            userr = Student.objects.all()
            dept = 'All'
            context = {
                'students':userr,
                'dept' : dept
            }

            return render(request,'company/find_candidate.html',context)
    else:
        return redirect('/company/login')

def CompanyFindCandidate(request):
    if request.user.is_authenticated and request.user.is_company:
        userr = Student.objects.all()
        skill =  Skill_list.objects.all()
        try:
            own_skill = Skills.objects.all()
            # skill_li = own_skill.skills.split(',')
        except:
            own_skill = None
            # skill_li = []

        context = {
            'students':userr,
            'skills' : skill,
            'own_skill' : own_skill
        }
        return render(request,"company/find_candidate.html",context)
    else:
        return redirect('/company/login')


def CompanyProjectView(request):
    if request.user.is_authenticated and request.user.is_company:
        project = Project.objects.all()
        
        context = {
            'projects':project
        }
        return render(request,"company/project_see.html",context)
    else:
        return redirect('company/login')


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



def CompanyStudentProfileView(request,slug):
    if request.user.is_authenticated and request.user.is_company:
        skill =  Skill_list.objects.all()
        try:
            stu = Student.objects.get(Id_number = slug)
            own_skill = Skills.objects.get(username = slug)
            skill_li = own_skill.skills.split(',')
            achievements = Achievement.objects.filter(student_name=slug)
            project = Project.objects.filter(student_name = slug)
            mark = Marks.objects.get(id_no = slug)
        except:
            stu = None
            own_skill = None
            skill_li = []
            achievements = None
            project = None
            mark = None
        
        # if stu is not None:
        context={
            'student':stu,
            'achievements' : achievements,
            'projects': project,
            'marks' : mark,
            'skills':skill,
            'own_skill':skill_li
        }
        return render(request,'company/stu_profile.html',context)
    else:
        return redirect('/company/login')

def CompanyProfileUpdateView(request,slug):
    if request.method == "POST":
        # skills = request.POST.get('skills')
        # skil = dict(Student.boolschoice)
        # skill = [skil[t] for t in skills]
        
        cname = request.POST.get('cname')
        year_of_found = request.POST.get('year_of_found')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        work_field = request.POST.get('work_field')
        no_of_emp = request.POST.get('no_of_emp')
        description = request.POST.get('description')
            # role = request.POST.get('role')

        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        country = request.POST.get('country')
        website = request.POST.get('website')
        fb_link = request.POST.get('fb_link')
        linkedin_link = request.POST.get('linkedin_link')
        insta_link = request.POST.get('insta_link')
            
        try:
            
            userr = Company.objects.get(company_username = request.user.username)
            userr.company_name = cname
            userr.year_found = year_of_found
            userr.email = email
            userr.mobile = mobile
            userr.field_name = work_field
            userr.no_of_employee = no_of_emp
            userr.description = description
            userr.address = address
            userr.state = state
            userr.city = city
            userr.country = country
            userr.website = website
            userr.fb_profile = fb_link
            userr.insta_profile = insta_link
            userr.linkedin_profile = linkedin_link
            
            
            userr.save()
            messages.success(request,"Updated")
            url = '/company/profile/'+str(slug)
            return redirect(url)


            
        except:
            form = Company.objects.create(company_username = request.user.username,company_id=slug,company_name=cname,no_of_employee= no_of_emp,field_name=work_field,mobile=mobile,email=email,year_found=year_of_found,description=description,address=address,state=state,city=city,country=country,website=website,fb_profile=fb_link,insta_profile=insta_link,linkedin_profile=linkedin_link)
            # for word in skill:
            #     form.skills.add(word)
            # form.skills.set(skill)
            form.save()
            messages.success(request,"Inserted")

        
            url = '/company/profile/'+str(slug)
            return redirect(url)

    
    else:
        url = '/company/profile/'+str(slug)
        return redirect(url)
        



def CompanyProfileView(request,slug):
    if request.user.is_authenticated and request.user.is_company:
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
            userr = Company.objects.get(company_id=slug)
        except:
            userr = None
        context={
                'company' : userr
        }
        return render(request,"company/profile.html",context)

        
        
        
    
          
    # else:
    #     return HttpResponse("<h1>not happening</h1>")
            

            # return redirect('/students/profile') 
            # return render(request,"students/index.html")

        
        # return render(request,"students/profile.html")
   
    else:
        return redirect('company/login')
     