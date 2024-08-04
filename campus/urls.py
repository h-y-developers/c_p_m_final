from django.urls import path,include
# from .views import (
# 	StudentDashboardView,
# 	StudentExamView,
# 	StudentTimetableView,
# 	StudentProjectView,
# 	StudentAssignmentView,
# 	StudentAchievementView,
# 	StudentMaterialView,
# 	FacultyDashboardView,
# 	FacultyProfileView,
# 	FacultyMarksView,
# 	FacultyMaterialsView,
# 	FacultyStudentDataView,
# 	FacultyAssignmentView,
# 	FacultyViewAssignmentView,
#     AdminAddAdminView,
#     AdminCompanyView,
#     AdminFacultyView,
#     AdminStudentView,
#     AdminLoginView,
#     AdminLogoutView,
#     # initial_login,
#     StudentProfileView,



# )

# from .views import



# from .views import college,c_admin,faculty,student


# from .views.c_admin import (AdminForgetPassView,AdminLogoutView,AdminLoginView,AdminStudentView, AdminFacultyView, AdminAddAdminView,AdminCompanyView)

from .views.student import (like_project,skills,StudentProjectsee,StudentProfileUpdateView,StudentCertificateView,StudentForgetPassView,StudentLogoutView,StudentLoginView,StudentProfileView, StudentDashboardView,StudentAchievementView,StudentExamView,StudentAddProjectView,StudentEventView,Studentproject,StudentProfileSettingView)

from .views.c_admin import (AdminForgetPassView,AdminLogoutView,AdminLoginView,AdminStudentView, AdminFacultyView, AdminAddAdminView,AdminCompanyView,AdminStudentMarksView,AdminProfileSettingView)

from .views.company import (CompanyStudentProfileView,CompanyProfileView,CompanyProfileUpdateView,CompanyProjectView,CompanyForgetPassView,CompanyLoginView,CompanyLogoutView,CompanyDashboardView,CompanyFindCandidate,CompanyRequirements,CompanyProfileSettingView,CompanyFindCandidateFilter)

from .views.faculty import (FacultyForgetPassView,FacultyLogoutView,FacultyLoginView,FacultyDashboardView,FacultyProfileView,FacultyEventView,FacultyAddEventView,FacultyProfileSettingView,FacultyEditEventView,FacultyDeleteEventView)

from .views.college import (home,LogoutView,ForgetPasswordView,ActivateView,ChangePasswordView,ProfileSettingView)

from .views.file_upload import (simple_upload)
from django.contrib.auth import views as auth_views
app_name = 'campus'

urlpatterns = [
    # path('/',shome,name="initial_login"),
    path('',home,name="login"),
    # url(r'login/',home,name="login"),
    # path('',college.home,name="home"),
    # path('students/', include(([
    #     # path('', student.StudentLoginView, name='student_login'),
    #     # path('logout/',student.StudentLogoutView,name='student_logout'),
    #     # path('login/', student.StudentLoginView, name='student_login'),
    #     path('index/', student.StudentDashboardView, name='student_dashboard'),
    #     path('events/', student.StudentEventView, name='student_event'),
    #     path('achievements/', student.StudentAchievementView, name='student_achievements'),
    #     path('exams/', student.StudentExamView, name='student_exams'),
    #     path('projects/', student.StudentProjectView, name='student_projects'),
    #     path('profile/', student.StudentProfileView, name='student_profile'),
        
    # ], 'campus'), namespace='students')),



    # path('faculty/', include(([
    #     # path('', faculty.FacultyLoginView, name='faculty_login'),
    #     # path('logout/',faculty.FacultyLogoutView,name='faculty_logout'),
    #     # path('login/', faculty.FacultyLoginView, name='faculty_login'),
    #     path('index/', faculty.FacultyDashboardView.as_view(), name='faculty_dashboard'),
    #     path('events/', faculty.FacultyEventView.as_view(), name='faculty_events'),
    #     path('add_event/', faculty.FacultyAddEventView.as_view(), name='faculty_add_events'),
    #     path('profile/', faculty.FacultyProfileView.as_view(), name='faculty_profile'), 
    # ], 'campus'), namespace='faculties')),


    # path('c_admin/', include(([
    #     # path('', c_admin.AdminLoginView, name='admin_login'),
    #     # path('logout/',AdminLogoutView,name='admin_logout'),
    #     path('login/', c_admin.AdminLoginView, name='admin_login'),
    #     path('add_admin/', c_admin.AdminAddAdminView, name='admin_add_admin'),
    #     path('add_company/', c_admin.AdminCompanyView, name='admin_add_company'),
    #     path('add_faculty/', c_admin.AdminFacultyView, name='admin_add_faculty'),
    #     path('add_student/', c_admin.AdminStudentView, name='admin_add_student'), 
    # ], 'campus'), namespace='c_admin')),
    # path('/',initial_login,name='login_init'),
    # url(r'^login/$', auth_views.login ,{'template_name': 'C_Admin/login.html'}, name='login'),
    # path('students/profile', student.StudentProfileView, name="student_profile"),
    # path('students/', student.StudentDashboardView, name='student_dashboard'),
    # path('students/index', student.StudentDashboardView, name='student_dashboard'),
    # path('students/exams', student.StudentExamView, name='student_exams'),
    # # path('students/assignments', StudentAssignmentView, name='student_assignments'),
    # path('students/projects', student.StudentProjectView, name='student_projects'),
    # # path('students/timetable', StudentTimetableView, name='student_timetable'),
    # path('students/achievements', student.StudentAchievementView, name='student_achievements'),
    
    path('students/login',StudentLoginView,name="student_login"),

    path('students/profile/<str:slug>', StudentProfileView, name="student_profile"),

    # path('students/profile/<str:slug>/add_skill', insertSkill, name="add_skill"),
    path('students/profile/<str:slug>/update', StudentProfileUpdateView, name="student_update_profile"),
    # path('students/profile_see', StudentProjectsee, name="student_profile_see"),
    path('students/', StudentDashboardView, name='student_dashboard'),
    path('students/index', StudentDashboardView, name='student_dashboard'),
    path('students/exams', StudentExamView, name='student_exams'),
    path('students/add_achievement', StudentCertificateView, name='student_cerificate'),
    path('students/skills',skills,name="Skills_achievement"),
    # path('students/profile_submit', StudentProfileView, name="student_profile_submit"),
    # path('students/profile', StudentProfileadd, name="student_profile"),
    # path('students/', StudentDashboardView, name='student_dashboard'),
    # path('students/index', StudentDashboardView, name='student_dashboard'),
    # path('students/exams', StudentExamView, name='student_exams'),
    # path('students/certi', StudentCertificateadd, name='student_cerificate'),

    # path('students/certi_submit', StudentCertificateView, name='student_cerificate_submit'),
    # path('students/assignments', StudentAssignmentView, name='student_assignments'),
    path('students/add_project', StudentAddProjectView, name='student_projects'),
    # path('students/projects_submit', Studentproject, name='student_submit_projects'),
    path('students/projects', Studentproject, name='student_add_projects'),
    path('students/project_see', StudentProjectsee, name="student_project_see"),
    # path('students/timetable', StudentTimetableView, name='student_timetable'),
    path('students/achievements', StudentAchievementView, name='student_achievements'),
    path('students/edit_profile/<str:slug>', StudentProfileSettingView, name='student_profile_setting'),
    
    path('students/events', StudentEventView, name='student_Events'),

    # path('students/certi', StudentCertificateView, name='student_achievements'),
    path('students/logout', StudentLogoutView, name='student_logout'),
    path('students/forgetPassword', StudentForgetPassView, name='student_forget'),
    # path('students/materials', StudentMaterialView, name='student_materials'),
    path('faculty/login',FacultyLoginView,name="faculty_login"),
    path('faculty/', FacultyDashboardView, name='faculty_dashboard'),
    path('faculty/index', FacultyDashboardView, name='faculty_dashboard'),
    path('faculty/profile', FacultyProfileView, name='faculty_profile'),
    path('faculty/add_event', FacultyAddEventView, name='faculty_add_event'),
    path('faculty/events', FacultyEventView, name='faculty_events'),
    path('faculty/logout', FacultyLogoutView, name='faculty_logout'),
    path('faculty/forgetPassword', FacultyForgetPassView, name='faculty_forget'),
    path('faculty/edit_profile/<str:slug>', FacultyProfileSettingView, name='faculty_profile_setting'),
    path('faculty/edit_event/<str:slug>', FacultyEditEventView, name='faculty_edit_event'),
    path('faculty/delete_event/<str:slug>', FacultyDeleteEventView, name='faculty_delete_event'),
    path('faculty/events', FacultyEventView, name='faculty_Events'),
    # path('faculty/materials', FacultyMaterialsView, name='faculty_material'),
    # path('faculty/view_Marks', FacultyMarksView, name='faculty_marks'),
    # path('faculty/student_data', FacultyStudentDataView, name='faculty_student_data'),
    # path('c_admin/add_student1',simple_upload, name="upload_excel_data"),
    path('c_admin/', AdminAddAdminView, name='admin_dashboard'),
    path('c_admin/index', AdminAddAdminView, name='admin_add_admin'),
    path('c_admin/add_company', AdminCompanyView, name='admin_add_company'),
    path('c_admin/add_faculty', AdminStudentMarksView, name='admin_add_faculty'),
    path('c_admin/add_student', AdminStudentView, name='admin_add_student'),
    path('c_admin/login',AdminLoginView,name='admin_login'),
    path('c_admin/logout',AdminLogoutView,name='admin_logout'),
    path('c_admin/forgetPassword',AdminForgetPassView,name='admin_forget'),
    path('c_admin/edit_profile/<str:slug>', AdminProfileSettingView, name='admin_profile_setting'),
    path('logout/',LogoutView,name='logout'),


    path('company/login',CompanyLoginView,name="company_login"),
    path('company/index', CompanyDashboardView, name='company_dashboard'),
    path('company/logout', CompanyLogoutView, name='company_logout'),
    path('company/Find_candidate', CompanyFindCandidate, name='company_findcandidate'),
    path('company/Find_candidate/filter', CompanyFindCandidateFilter, name='company_findcandidate_filter'),
    path('company/requirements', CompanyRequirements, name='company_requirements'),
    path('company/forgetPassword', CompanyForgetPassView, name='company_forget'),
    path('company/project_see', CompanyProjectView, name='company_projects'),
    path('company/profile/<str:slug>', CompanyProfileView, name='company_profile'),
    path('company/profile/<str:slug>/update', CompanyProfileUpdateView, name='company_edit_profile'),
    path('company/edit_profile/<str:slug>', CompanyProfileSettingView, name='company_profile_setting'),
    path('company/student/<str:slug>', CompanyStudentProfileView, name='company_student_profile'),
    path('forgetPassword',ForgetPasswordView,name="forget_password"),

    # path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     activate, name='activate'),
    path('activate/<slug:slug>/<slug:token>',ActivateView,name="activate_link"),
    path('changePassword/<str:slug>',ChangePasswordView,name="change_password"),
    path('profile_setting/<str:slug>',ProfileSettingView,name="profile_setting"),
    path('likes',like_project,name="liked")
    # path('c_admin/', c_admin.AdminAddAdminView, name='admin_dashboard'),
    # path('c_admin/index', c_admin.AdminAddAdminView, name='admin_add_admin'),
    # path('c_admin/add_company', c_admin.AdminCompanyView, name='admin_add_company'),
    # path('c_admin/add_faculty', c_admin.AdminFacultyView, name='admin_add_faculty'),
    # path('c_admin/add_student', c_admin.AdminStudentView, name='admin_add_student'),
    # path('c_admin/login',c_admin.AdminLoginView,name='admin_login'),
    # path('c_admin/logout',c_admin.AdminLogoutView,name='admin_logout'),
    # path('forgetPassword',ForgetPasswordView,name="forget_password"),

    # path('logout/',LogoutView,name='logout'),
    # path('changePassword',ChangePasswordView,name="change_password")

#     url(r'students/login',StudentLoginView,name="student_login"),
#     url(r'students/profile', StudentProfileView, name="student_profile"),
#     url(r'students/', StudentDashboardView, name='student_dashboard'),
#     url(r'students/index', StudentDashboardView, name='student_dashboard'),
#    url(r'students/exams', StudentExamView, name='student_exams'),
#     # path('students/assignments', StudentAssignmentView, name='student_assignments'),
#     url(r'students/projects', StudentProjectView, name='student_projects'),
#     # path('students/timetable', StudentTimetableView, name='student_timetable'),
#     url(r'students/achievements', StudentAchievementView, name='student_achievements'),
#     url(r'students/logout', StudentLogoutView, name='student_logout'),
#     url(r'students/forgetPassword', StudentForgetPassView, name='student_forget'),
#     # path('students/materials', StudentMaterialView, name='student_materials'),
#     url(r'faculty/login',FacultyLoginView,name="faculty_login"),
#     url(r'faculty/', FacultyDashboardView, name='faculty_dashboard'),
#     url(r'faculty/index', FacultyDashboardView, name='faculty_dashboard'),
#     url(r'faculty/profile', FacultyProfileView, name='faculty_profile'),
#     url(r'faculty/add_event', FacultyAddEventView, name='faculty_add_event'),
#     url(r'faculty/events', FacultyEventView, name='faculty_events'),
#     url(r'faculty/logout', FacultyLogoutView, name='faculty_logout'),
#     url(r'faculty/forgetPassword', FacultyForgetPassView, name='faculty_forget'),
#     # path('faculty/materials', FacultyMaterialsView, name='faculty_material'),
#     # path('faculty/view_Marks', FacultyMarksView, name='faculty_marks'),
#     # path('faculty/student_data', FacultyStudentDataView, name='faculty_student_data'),
#     url(r'c_admin/', AdminAddAdminView, name='admin_dashboard'),
#     url(r'c_admin/index', AdminAddAdminView, name='admin_add_admin'),
#     url(r'c_admin/add_company', AdminCompanyView, name='admin_add_company'),
#     url(r'c_admin/add_faculty', AdminFacultyView, name='admin_add_faculty'),
#     url(r'c_admin/add_student', AdminStudentView, name='admin_add_student'),
#     url(r'c_admin/login',AdminLoginView,name='admin_login'),
#     url(r'c_admin/logout',AdminLogoutView,name='admin_logout'),
#     url(r'c_admin/forgetPassword',AdminForgetPassView,name='admin_forget'),
#     url(r'logout/',LogoutView,name='logout'),


#     url(r'forgetPassword',ForgetPasswordView,name="forget_password"),

#     # path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
#     url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#         activate, name='activate'),
#     url(r'changePassword',ChangePasswordView,name="change_password")
]
