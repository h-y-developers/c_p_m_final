from django import forms
from .models import Student

class DocumentForm(forms.Form):
    certi = forms.FileField(
        label="upload files"
    )


# class SkillForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('skills',)
#         widgets = {
#             'interests': forms.MultiSelectField
#         }

