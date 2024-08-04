from django.contrib import messages
from django.contrib.auth import login,  authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView,View
from django.http import HttpResponse
from .resources import studentResource,studentmarksResource
from tablib import Dataset


from ..decorators import admin_required
from ..models import College, User, Student,Marks


# @method_decorator([login_required, admin_required], name='dispatch')
# class AdminLoginView(View):
#     model = User
#     # form_class = StudentInterestsForm
#     template_name = 'C_Admin/login.html'
#     success_url = reverse_lazy('c_admin:admin_login')


# @method_decorator([login_required, admin_required], name='dispatch')
# class AdminAddAdminView(View):
#     model = User
#     # form_class = StudentInterestsForm
#     template_name = 'C_Admin/admin.html'
#     success_url = reverse_lazy('c_admin:admin_add_admin')


# @method_decorator([login_required, admin_required], name='dispatch')
# class AdminCompanyView(View):
#     model = User
#     # form_class = StudentInterestsForm
#     template_name = 'C_Admin/company_id.html'
#     success_url = reverse_lazy('c_admin:admin_add_company')


# @method_decorator([login_required, admin_required], name='dispatch')
# class AdminFacultyView(View):
#     model = User
#     # form_class = StudentInterestsForm
#     template_name = 'C_Admin/faculty_id.html'
#     success_url = reverse_lazy('c_admin:admin_add_faculty')


# @method_decorator([login_required, admin_required], name='dispatch')
# class AdminStudentView(View):
#     model = User
#     # form_class = StudentInterestsForm
#     template_name = 'C_Admin/student_id.html'
#     success_url = reverse_lazy('c_admin:admin_add_student')





def AdminLoginView(request):
    if request.user.is_authenticated:
        return redirect('/c_admin/index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            if username == "" or password == "":
                messages.error(request,"Please fill all the fields")
                return redirect('/c_admin/login')
            else:    
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_admin:
                        login(request, user)
                        return redirect('/c_admin/index')
                    else:
                        messages.error(request, 'You are not authorized as admin')   
                else:
                    messages.error(request, 'Username Or Password is incorrect')
                    return redirect('/c_admin/login')
            
        context = {}
        return render(request, 'c_admin/login.html', context)




# def AdminAddAdminView(request):
#     return render(request,"C_Admin/admin.html")

# def AdminCompanyView(request):
#     return render(request,"C_Admin/company_id.html")

# def AdminFacultyView(request):
#     return render(request,"C_Admin/faculty_id.html")

# def AdminStudentView(request):
#     return render(request,"C_Admin/student_id.html")



# @method_decorator([login_required, admin_required], name='dispatch')
# def AdminLoginView(request):
#     return render(request,'C_Admin/login.html')


# @method_decorator([login_required, admin_required], name='dispatch')

def AdminLogoutView(request):
    return redirect('/logout')

def AdminForgetPassView(request):
    return redirect('/forgetPassword')


def AdminAddAdminView(request):
    if request.user.is_authenticated and request.user.is_admin:
        return render(request,"c_admin/admin.html")
    else:
        return redirect('/c_admin/login')


# @method_decorator([login_required, admin_required], name='dispatch')
def AdminCompanyView(request):
    if request.user.is_authenticated and request.user.is_admin:
        return render(request,"c_admin/company_id.html")
    else:
        return redirect('/c_admin/login')


# @method_decorator([login_required, admin_required], name='dispatch')
def AdminFacultyView(request):
    if request.user.is_authenticated and request.user.is_admin:
        return render(request,"c_admin/faculty_id.html")
    else:
        return redirect('/c_admin/login')




FILE_FORMAT = ['xlsx','xls']
# @method_decorator([login_required, admin_required], name='dispatch')
def AdminStudentView(request):
    if request.user.is_authenticated and request.user.is_admin:
        if request.method == "POST" and 'xl_data' in request.FILES:

            student_resource = studentResource()
            dataset = Dataset()
            new_persons = request.FILES['xl_data']
            # doc = new_persons
            file_type = new_persons.name
            file_type = file_type.lower()
            if not file_type.endswith(".xlsx"):
                messages.error(request,"Please upload xlsx or xls file")
                return redirect('/c_admin/add_student')
            else:
                try:
                    imported_data = dataset.load(new_persons.read(),format='xlsx')
                    
                    for data in imported_data:
                        user = User(
                            data[0],
                            username = data[1],
                            first_name = data[2],
                            last_name = data[3],
                            email = data[4],
                            dept = data[5],
                            is_student = True
                           )
                        student = Marks(
                            id_no = data[1]
                        )
                        # student = Student(
                                
                        #         Id_number = data[1]

                        #     )

                        user.set_password('Bvm@12345')
                        student.save()    
                        user.save()

                    messages.success(request,"File Uploaded")
                    return redirect("/c_admin/add_student")  
                except Exception as e:
                    # messages.error(request,"Some Entry is repeated")
                    messages.error(request,e)
                    return redirect("/c_admin/add_student")    
                 
        else:
            return render(request,"c_admin/student_id.html")


                    
            # result = student_resource.import_data(dataset, dry_run=True)  # Test the data import

            # if not result.has_errors():
            #    student_resource.import_data(dataset, dry_run=False)  # Actually import now

        
    else:
        return redirect('/c_admin/login')


FILE_FORMAT = ['xlsx','xls']
# @method_decorator([login_required, admin_required], name='dispatch')
def AdminStudentMarksView(request):
    if request.user.is_authenticated and request.user.is_admin:
        if request.method == "POST" and 'xl_data' in request.FILES:

            student_marks_resource = studentmarksResource()
            dataset = Dataset()
            new_marks = request.FILES['xl_data']
            # doc = new_persons
            file_type = new_marks.name
            file_type = file_type.lower()
            if not file_type.endswith(".xlsx"):
                messages.error(request,"Please upload xlsx or xls file")
                return redirect('/c_admin/add_faculty')
            else:
                try:
                    imported_data = dataset.load(new_marks.read(),format='xlsx')
                    
                    for data in imported_data:
                        # print(data[0])
                        user = Marks.objects.get(id_no = data[1])
                        # user = Marks(
                        #     data[0],
                        #     id_no = data[1],
                        #     sem_1 = data[2],
                        #     sem_2 = data[3],
                        #     sem_3 = data[4],
                        #     sem_4 = data[5],
                        #     sem_5 = data[6],
                        #     sem_6 = data[7],
                        #     sem_7 = data[8],
                        #     sem_8 = data[9],
                        #     first_year = data[10],
                        #     second_year = data[11],
                        #     third_year = data[12],
                        #     fourth_year = data[13],
                        #     # is_student = True
                        #    )

                        user.id_no = data[1]
                        user.sem_1 = data[2]
                        user.sem_2 = data[3]
                        user.sem_3 = data[4]
                        user.sem_4 = data[5]
                        user.sem_5 = data[6]
                        user.sem_6 = data[7]
                        user.sem_7 = data[8]
                        user.sem_8 = data[9]
                        user.first_year = data[10]
                        user.second_year = data[11]
                        user.third_year = data[12]
                        user.fourth_year = data[13]
                        user.save()

                    messages.success(request,"File Uploaded")
                    return redirect("/c_admin/add_faculty")  
                except:
                    messages.error(request,"Some Entry is repeated")
                    return redirect("/c_admin/add_faculty")    
                 
        else:
            return render(request,"c_admin/faculty_id.html")


                    
            # result = student_resource.import_data(dataset, dry_run=True)  # Test the data import

            # if not result.has_errors():
            #    student_resource.import_data(dataset, dry_run=False)  # Actually import now

        
    else:
        return redirect('/c_admin/login')


def export(request):
    student_resource1 = studentResource()
    dataset = student_resource1.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="student.xls"'
    return response



def AdminProfileSettingView(request,slug):
    if request.user.is_authenticated and request.user.is_admin:
        userr = User.objects.get(slug = slug)
        if request.method == "POST" and request.FILES['profile_pic']:
            profile_img = request.FILES['profile_pic']
            userr.profile_pic = profile_img
            userr.save()
            
            return redirect('/c_admin/index')
        else:
            context ={
            'admin':userr
            }
            return render(request,"c_admin/edit_profile.html",context)
    else:
        return redirect('/c_admin/login')