from django.shortcuts import render
from .models import*
from .forms import*
from seeker.models import *
from seeker.models import addfeedback
from jobadmin.models import*
from django.http import HttpResponse
def index (request):
    return render(request,'providerhome.html')
def base (request):
    return render(request,'providerhome.html')
def logins(request):
    loginform=loginForms()
    return render (request,'login.html',{'form':loginform})
def providerhomes(request):
    return render(request,'providerhome.html')

def addvacancy(request,id):
    if request.method=="GET":
        vacancy=vacancyForm()
        return render(request,'addvacancy.html',{'form':vacancy})
    else:
        vacancy=vacancyForm(request.POST,request.FILES)
        if vacancy.is_valid():
            providerid=id
            print("providerid", providerid)
            obj=vacancy.save(commit=False)
            obj.provider_id_id=providerid
            obj.save()
        #vacancy=vacancyForm()
        return render(request,'providerhome.html')

def feedbackviews (request):
    id=request.session['id']
    seeker_feedback=addfeedback.objects.all()
    return render(request,'feedbackview.html',{'obj':seeker_feedback})
def vacancyrequest (request):
    obj=applications.objects.filter(vacancy_id__in=(vacancy.objects.filter(provider_id_id=request.session["id"])))
    print("hai",obj)
    print("provider id",request.session["id"])
    
   # print("vacancy id",request.session["id"])
    return render(request,"viewrequest.html",{'obj':obj})
def readfiles(request,id):
    print (id)
    id=12
    detail = seekerregistration.objects.values_list('id', 'resume')
    f = open(detail, 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain") 
def vacancyviews (request):
    id=request.session['id']
    provider_vacancy=vacancy.objects.filter(provider_id_id=id)
    return render(request,'editvacancy.html',{'obj':provider_vacancy})
def deletes(request,id):
    vacancy.objects.filter(id=id).delete()
    return render(request,'providerhome.html')       


    

    
    

    
    


