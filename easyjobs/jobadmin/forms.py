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
class seekerregistrationForms(forms.ModelForm):
    class Meta:
        model=seekerregistration
        fields='__all__'
        label={
            'firstname':'first name',
            'lastname':'last name',
            'contact':'phone number',
            'dob':'date of birth',
            'address':'enter address',
            'resume':'upload resume',
            'email':'email',
            'password':'password',

        }
    confirm_password=forms.CharField(max_length=100, required=True)  
    def clean_confirm_password(self):
        print("inside validation")
        cp=self.cleaned_data.get('confirm_password')
        print("cp:",cp)
        pwd=self.cleaned_data.get('password')
        print("pwd",pwd)
        if cp!=pwd:
            print("checking")
            raise forms.ValidationError('Invalid value')
        return pwd
      #email validation
    def clean_email(self):
        testemail=self.cleaned_data['email']
        if seekerregistration.objects.filter(email=testemail).exists():
            raise forms.ValidationError('Email Already Existing')
        return testemail    
    
           
""" class loginForms(forms.ModelForm):
    class Meta:
        model=userlogin #table name
        fields="_all_"
        label={
            'email':'ENter valid email',
            'password':'enter valid password'
        } """
class providerregistrationForms(forms.ModelForm):
    class Meta:
        model=providerregistration
        fields='__all__'
        exclude=('status',)
        label={
            'name':'company name',
            'contact':'phone number',
            'address':'enter address',
            'businesslicense':'upload license',
            'description':'about your company',
            'email':'email',
            'password':'password',

        } 
    confirm_password=forms.CharField(max_length=100, required=True)  
    def clean_confirm_password(self):
        print("inside validation")
        cp=self.cleaned_data.get('confirm_password')
        print("cp:",cp)
        pwd=self.cleaned_data.get('password')
        print("pwd",pwd)
        if cp!=pwd:
            print("checking")
            raise forms.ValidationError('Invalid value')
        return pwd
      #email validation
    def clean_email(self):
        testemail=self.cleaned_data['email']
        if providerregistration.objects.filter(email=testemail).exists():
            raise forms.ValidationError('Email Already Existing')
        return testemail    
    
           
""" class loginForms(forms.ModelForm):
    class Meta:
        model=userlogin #table name
        fields="_all_"
        label={
            'email':'ENter valid email',
            'password':'enter valid password'
        } """    
class freelanceregistrationForms(forms.ModelForm):
    class Meta:
        model=freelanceregistration
        fields='__all__'
        exclude=('status',)
        label={
            'name':'name',
            'contact':'phone number',
            'address':'enter address',
            'resume':'upload resume',
            'email':'email',
            'password':'password',

        }             
    confirm_password=forms.CharField(max_length=100, required=True)  
    def clean_confirm_password(self):
        print("inside validation")
        cp=self.cleaned_data.get('confirm_password')
        print("cp:",cp)
        pwd=self.cleaned_data.get('password')
        print("pwd",pwd)
        if cp!=pwd:
            print("checking")
            raise forms.ValidationError('Invalid value')
        return pwd
      #email validation
    def clean_email(self):
        testemail=self.cleaned_data['email']
        if freelanceregistration.objects.filter(email=testemail).exists():
            raise forms.ValidationError('Email Already Existing')
        return testemail    
    
           
""" class loginForms(forms.ModelForm):
    class Meta:
        model=userlogin #table name
        fields="_all_"
        label={
            'email':'ENter valid email',
            'password':'enter valid password'
        } """