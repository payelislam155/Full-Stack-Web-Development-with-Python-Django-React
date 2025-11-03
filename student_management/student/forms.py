from django import forms
from . import models

class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = models.Student
        fields = "__all__"
        labels = {
            'name': 'Full Name',
            'photo': 'Upload Photo', 
            # 'inputEmail': 'Email',
            # 'inputPhone': 'Phone',
            # 'inputPassword': 'XXXXXXXX',
            # 'checkbox': 'Checkbox',
        }
        help_texts = {
            # 'name': 'Enter your full name',
            # 'photo': 'Upload your photo',
            'inputEmail': 'Enter your email',
            # 'inputPhone': 'Enter your phone number',
            # 'inputPassword': 'XXXXX your password',
            # 'checkbox': 'Check this box if you want to receive our newsletter',
        }

