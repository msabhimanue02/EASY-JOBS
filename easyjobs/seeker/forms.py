from django import forms
from .models import *
from django.forms import ModelForm
class loginForms(forms.ModelForm):
    class Meta:
        model=login
        fields={
            "email",
            "password"
        }
        label={
            'email':'Enter valid email',
            'password':'enter valid password'
        }
class addfeedbackForm(forms.ModelForm):
    class Meta:
        model=addfeedback
        fields='__all__'
        exclude=('seeker_id',)
        label={
            'title':'about the job',
            'description':'about your company',
        }