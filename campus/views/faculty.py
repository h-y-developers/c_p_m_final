# from django.shortcuts import render,HttpResponse,redirect
# from .models import Admin,Achievements,Assignments,Assign_record,College,Comapnies,Department,Faculties,Projects,Students,Subjects,Timetable,User_info
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView,View


from ..decorators import teacher_required
from ..models import  Faculties, Events, User


def FacultyLoginView(request):
    if request.user.is_authenticated:
        return redirect('/faculty/index')
    else:
        if request.method == 'POST':
            username = request.POST.get('fusername')
            password =request.POST.get('fpassword')
            user = authenticate(request, username=username, password=password)
            if username == "" or password == "":
                messages.error(request,"Please fill all the fields")
                return redirect('/faculty/login')
            else:    
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_faculty:
                        login(request, user)
                        return redirect('/faculty/index')
                    else:
                        messages.error(request,"You are not authorized as faculty")   
                else:
                    messages.error(request,"Username Or Password is incorrect")
                    return redirect('/faculty/login')
            
        context = {}
        return render(request, 'faculty/login.html', context)


def FacultyLogoutView(request):
    return redirect('/logout')


def FacultyForgetPassView(request):
    return redirect('/forgetPassword')

def FacultyDashboardView(request):
    if request.user.is_authenticated and request.user.is_faculty:
        return render(request,"faculty/faculty_index.html")
    else:
        return redirect('faculty/login')


def FacultyProfileView(request):
    if request.user.is_authenticated and request.user.is_faculty:
        if request.method == "POST" or 'B_E_college_result' in request.FILES or 'M_E_college_result' in request.FILES:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            # role = request.POST.get('role')
            dept = request.POST.get('dept')
            # enrollment = request.POST.get('enrollment')
            id_no = request.POST.get('id_no')
            desg = request.POST.get('desg')
            permanent_address = request.POST.get('permanent_address')
            state = request.POST.get('state')
            resident_address = request.POST.get('resident_address')
            pincode = request.POST.get('pincode')
            city = request.POST.get('city')
            country = request.POST.get('country')
            B_E_college_name =request.POST.get('B_E_college_name')
            B_E_college_result= request.FILES['B_E_college_result']
            M_E_college_name =request.POST.get('M_E_college_name')
            M_E_college_result= request.FILES['M_E_college_result']
            

            

            form = Faculties(fname=fname,lname=lname,gender=gender,dob=dob,email=email,
            mobile=mobile,dept=dept,id_no=id_no,desg=desg,
            permanent_address=permanent_address,state=state,resident_address=resident_address,
            pincode=pincode,city=city,country=country,B_E_college_name=B_E_college_name,
            B_E_college_result=B_E_college_result,M_E_college_name=M_E_college_name,M_E_college_result=M_E_college_result)
            form.save()
        return render(request,"faculty/faculty_profile.html")
    else:
        return redirect('faculty/login')

# def FacultyMarksView(request):
#     return render(request,"Faculty/marks.html")


# def FacultyMaterialsView(request):
#     return render(request,"Faculty/materials.html")

# def FacultyStudentDataView(request):
#     return render(request,"Faculty/student_data.html")

def FacultyAddEventView(request):
    if request.user.is_authenticated and request.user.is_faculty:
        if request.method == "POST" and 'poster' in request.FILES:
            event_name = request.POST.get('event')
            instructions = request.POST.get('instruction')
            url = request.POST.get('url')
            file = request.FILES['poster']
            event_date = request.POST.get('doe')
            form = Events(event_name=event_name,instructions=instructions,url=url,file=file,event_date=event_date)
           
            form.save()
            messages.success(request,"Event Uploaded")
        return render(request,'faculty/assign.html')
        # return render(request,"faculty/assign.html")
        
    else:
        return redirect('faculty/login')

def FacultyEventView(request):
    if request.user.is_authenticated and request.user.is_faculty:
        userr = Events.objects.all()
        context = {
            'events':userr
        }
        return render(request,"faculty/events_see.html",context)
    else:
        return redirect('/faculty/login')


def FacultyEditEventView(request,slug):
    if request.user.is_authenticated and request.user.is_faculty:
        if request.method == "POST":
            events = Events.objects.get(slug=slug)
            # print(request.FILES['poster'].name)
            # if request.session['event_poster'] == str(request.FILES['poster'].name):
            #     events.event_name = request.POST.get('event_name')
            #     events.instructions = request.POST.get('instructions')
            #     events.url = request.POST.get('url')
            #     # events.file = request.FILES['poster']
            #     events.event_date = request.POST.get('doe')
            # else:
            #     events.event_name = request.POST.get('event_name')
            #     events.instructions = request.POST.get('instructions')
            #     events.url = request.POST.get('url')
            #     events.file = request.FILES['poster']
            #     events.event_date = request.POST.get('doe')
            events.event_name = request.POST.get('event')
            events.instructions = request.POST.get('instructions')
            events.url = request.POST.get('url')
                # events.file = request.FILES['poster']
            events.event_date = request.POST.get('doe')
            
            events.save()
            messages.success(request,"Event Updated")
            return redirect("/faculty/events")
        else:
            userrr = Events.objects.get(slug = slug)
            context = {
                'event':userrr
            }
            request.session['event_poster'] = userrr.file.name
            print(request.session['event_poster'])
            return render(request,"faculty/edit_event.html",context)
    else:
        return redirect('/faculty/login')


def FacultyDeleteEventView(request,slug):
    if request.user.is_authenticated and request.user.is_faculty:
        userr = Events.objects.get(slug=slug)
        userr.delete()
        return redirect('/faculty/events')
        
    else:
        return redirect('/faculty/login')

def FacultyProfileSettingView(request,slug):
    if request.user.is_authenticated and request.user.is_faculty:
        userr = User.objects.get(slug = slug)
        if request.method == "POST" and request.FILES['profile_pic']:
            profile_img = request.FILES['profile_pic']
            userr.profile_pic = profile_img
            userr.save()
            
            return redirect('/faculty/index')
        else:
            context ={
            'faculty':userr
            }
            return render(request,"faculty/edit_profile.html",context)
    else:
        return redirect('/faculty/login')

# def AdminLogoutView(request):
#     logout(request)
#     return redirect('/c_admin/login')

# @method_decorator([login_required, teacher_required], name='dispatch')
# class FacultyDashboardView(View):
#     model = Faculties
#     # form_class = StudentInterestsForm
#     template_name = 'Faculty/faculty_index.html'
#     success_url = reverse_lazy('faculty:faculty_dashboard')

#     # def get_object(self):
#     #     return self.request.user.student

#     # def form_valid(self, form):
#     #     messages.success(self.request, 'Interests updated with success!')
#     #     return super().form_valid(form)


# # def StudentDashboardView(request):

# #     return render(request,"Student/index.html")

# # def StudentExamView(request):
# #     return render(request,"Student/exams.html")    

# # def StudentAssignmentView(request):
# #     return render(request,"Student/assignments.html")

# # def StudentProfileView(request):
# #     if request.method == "POST":
# #         fname = request.POST.get('fname')
# #         lname = request.POST.get('lname')
# #         gender = request.POST.get('gender')
# #         dob = request.POST.get('dob')
# #         email = request.POST.get('email')
# #         mobile = request.POST.get('mobile')
# #         role = request.POST.get('role')
# #         dept = request.POST.get('dept')
# #         form = Students(fname=fname,lname=lname,gender=gender,email=email,
# #         mobile=mobile,role=role,dept=dept)
# #         form.save()
# #         return render(request,"Student/index.html")
# #     # else:
# #     #     return HttpResponse("<h1>not happening</h1>")
            
    
# #     return render(request,"Student/form.html")   



# # def StudentProjectView(request):
# #     return render(request,"Student/projects.html")

# # def StudentTimetableView(request):
# #     return render(request,"Student/timetable.html")

# # def StudentAchievementView(request):
# #     return render(request,"Student/achievements.html")

# # def StudentMaterialView(request):
# #     return render(request,"Student/materials.html")


# @method_decorator([login_required, teacher_required], name='dispatch')
# class FacultyEventView(View):
#     model = Events
#     # form_class = StudentInterestsForm
#     template_name = 'Faculty/assignment_view.html'
#     success_url = reverse_lazy('faculty:faculty_events')


# @method_decorator([login_required, teacher_required], name='dispatch')
# class FacultyAddEventView(View):
#     model = Events
#     # form_class = StudentInterestsForm
#     template_name = 'Faculty/assign.html'
#     success_url = reverse_lazy('faculty:faculty_add_events')


# @method_decorator([login_required, teacher_required], name='dispatch')
# class FacultyProfileView(View):
#     model = Faculties
#     # form_class = StudentInterestsForm
#     template_name = 'Faculty/faculty_profile.html'
#     success_url = reverse_lazy('faculty:faculty_profile')


