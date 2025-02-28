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
class vacancyForm(forms.ModelForm):
    class Meta:
        model=vacancy
        fields='__all__'
        exclude=('provider_id',)
        label={
            'title':'title of the job',
            'qualification':'qualification of the seeker',
            'experience':'experience of the seeker',
            'salary': 'salary of the job',
            'vacancies':'number of vacancies',

        }
    def _init_(self,*args,**kargs):
        super()._init_(*args,**kargs)
        self.fields['provider_id'].empty_label="select"
