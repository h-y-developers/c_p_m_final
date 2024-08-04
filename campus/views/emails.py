from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from campus.tokens import account_activation_token
from django.views.generic import View
from ..models import User
from django.shortcuts import redirect
from django.contrib import messages


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.is_pass_change = True
            messages.success(request, ('Your password has been changed.'))
            return redirect('/login')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('/forgetPassword')