from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import logout, authenticate
from django.contrib import messages
from ..models import User,student_data
from Campus_Management_System.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token



def home(request):
    if request.user.is_authenticated:
        if request.user.is_faculty:
            return redirect('/faculty/index')
        elif request.user.is_student:
            return redirect('/students/index')
        elif request.user.is_company:
            return redirect('/company/index')
        else:
            return redirect('/c_admin/index')
    else:
        return redirect('/students/login')


def LogoutView(request):
    if request.user.is_faculty:
        logout(request)
        return redirect('/faculty/login')
    elif request.user.is_student:
        logout(request)
        return redirect('/students/login')
    elif request.user.is_company:
        logout(request)
        return redirect('/company/login')
    elif request.user.is_admin:
        logout(request)
        return redirect('/c_admin/login')
    else:
        logout(request)
        return redirect('/students/login')




def ForgetPasswordView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username == '':
            messages.error(request,"All fields are required")
            return redirect('/forgetPassword')
        else:
            if User.objects.filter(username=username).exists():
                user  = User.objects.get(username=username)
                recepient = user.email
                user.is_active = False
                current_site = get_current_site(request)
                subject = 'Change Your Account Password'
                token = account_activation_token.make_token(user)
                request.session['token']= token
                message = render_to_string('emails/email_authentication.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': user.slug,
                    'token': token,
                })
                send_mail(
                    subject,
                    message,
                    EMAIL_HOST_USER,
                    [recepient],
                    fail_silently=False,
                )
            
                messages.success(request,"Please check registered Email ID")
                return redirect('/forgetPassword')
            else:
                messages.error(request,"User does not exists")
                return redirect('/forgetPassword')
    else:
        context = {}
        return render(request,'forgetpass.html')



def ActivateView(request, slug, token):
    user = User.objects.get(slug=slug)
    if token == request.session['token']:
        context={
            slug:slug
        }
        url = '/changePassword/'+ str(slug) 
        return redirect(url)
    else:
        messages.error(request,'Invalid Link')
        return redirect('/forgetPassword')
    

def ChangePasswordView(request,slug):
    if request.method == 'POST':
        password = request.POST.get('password2')
        user = User.objects.get(slug=slug)
        user.set_password(password)
        user.save()
        messages.success(request,"Password has been changed.")
        return redirect('/student/slogin')

    else:
        context={
            slug:slug
        }
        return render(request,'changePassword.html',context)



def ProfileSettingView(request,slug):
    if request.user.is_authenticated:
        if request.user.is_faculty:
            url = '/faculty/edit_profile/'+slug
            return redirect(url)
        elif request.user.is_student:
            url = '/students/edit_profile/'+slug
            return redirect(url)
        elif request.user.is_company:
            url = '/company/edit_profile/'+slug
            return redirect(url)    
        else:
            url = '/c_admin/edit_profile/'+slug
            return redirect(url)
        return redirect('/students/login')



def ProfileSettingUpdateView(request,slug):
    if request.method == 'POST':
        password = request.POST.get('password2')
        user = User.objects.get(slug=slug)
        user.set_password(password)
        user.save()
        messages.success(request,"Password has been changed.")
        return redirect('/login')

    else:
        context={
            slug:slug
        }
        return render(request,'changePassword.html',context)





# class MainView(TemplateView):
#     template_name = 'sample_forms/index.html'

#     def get(self, request, *args, **kwargs):
#         question_form = QuestionForm(self.request.GET or None)
#         answer_form = AnswerForm(self.request.GET or None)
#         context = self.get_context_data(**kwargs)
#         context['answer_form'] = answer_form
#         context['question_form'] = question_form
#         return self.render_to_response(context)

# from django.utils.encoding import force_text
# from django.utils.http import urlsafe_base64_decode
# from .tokens import account_activation_token
# from django.views.generic import View


# class ActivateAccount(View):

#     def get(self, request, uidb64, token, *args, **kwargs):
#         try:
#             uid = force_text(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#             user = None

#         if user is not None and account_activation_token.check_token(user, token):
#             user.is_active = True
#             user.profile.is_pass_change = True
#             messages.success(request, ('Your password has been changed.'))
#             return redirect('/changePassword')
#         else:
#             messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
#             return redirect('/forgetPassword')


# # def ActivateAccount(self, request, uidb64, token, *args, **kwargs):
# #         try:
# #             uid = force_text(urlsafe_base64_decode(uidb64))
# #             user = User.objects.get(pk=uid)
# #         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
# #             user = None

# #         if user is not None and account_activation_token.check_token(user, token):
# #             user.is_active = True
# #             user.profile.is_pass_change = True
# #             messages.success(request, ('Your password has been changed.'))
# #             return redirect('/changePassword')
# #         else:
# #             messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
# #             return redirect('/forgetPassword')



# def activate(request, uidb64, token):
#     try:
#         uid = uidb64
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         # user.save()
#         messages.success(request,'Thank you for your email confirmation. Now you can login your account.')
#         return redirect('/changePassword/uid')
#         # login(request, user)
#         # return redirect('home')
#         # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         messages.error(request, ('The confirmation link was invalid, possibly because it has already been used.'))
#         return redirect('/forgetPassword')