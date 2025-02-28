from django.http import HttpResponse
from django.shortcuts import render
from seeker.models import addfeedback
from .models import *
from .forms import *
from provider.models import vacancy
from django.contrib import messages
def index (request):
    return render(request,'index.html')
def base (request):
    return render(request,'base.html')
def admins (request):
    return render(request,'admin.html')
""" def logins(request):
    loginform=loginForms()
    return render (request,'login.html',{'form':loginform}) """
def seekerregistrations(request):  
    args={}
    if request.method=="POST":
        form = seekerregistrationForms(request.POST,request.FILES)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            form.save()
            keyuser="JobSeeker"
            logindata=login(email=email,password=password,keyuser=keyuser)
            logindata.save()
            return render(request, 'login.html',{'form':loginForms})                   
    else:            
        form = seekerregistrationForms()
    args['form'] = form
    return render(request,'seekerreg.html', args)  
def providerregistrations(request):
 args={}
 if request.method=="POST":
        form = providerregistrationForms(request.POST,request.FILES)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            form.save()
            keyuser="JobProvider"
            logindata=login(email=email,password=password,keyuser=keyuser)
            logindata.save()
            return render(request, 'login.html',{'form':loginForms})                   
 else:            
        form = providerregistrationForms()
 args['form'] = form
 return render(request,'providerreg.html', args)  
def freelanceregistrations(request):
    args={}
    if request.method=="GET":
        form = freelanceregistrationForms()
        args['form'] = form
        return render(request,'freelancereg.html', args)
    else:
        form = freelanceregistrationForms(request.POST,request.FILES)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            form.save()
            keyuser="freeLance"
            logindata=login(email=email,password=password,keyuser=keyuser)
            logindata.save()
            return render(request, 'login.html',{'form':loginForms})                   

    form = freelanceregistrationForms()
    args['form'] = form
    return render(request,'freelancereg.html', args)

def logins(request):
    if request.method=="GET":
        loginform=loginForms()
        return render(request, 'login.html')
    else:
        loginform=loginForms()
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        if login.objects.filter(email=email,password=password).exists():
        
            userdetail=login.objects.get(email=email,password=password)
            if(userdetail.keyuser=='admin'):
                return render(request, 'admin.html')
            elif(userdetail.keyuser=='JobSeeker'):
                email=userdetail.email
                print("hai",email)
                obj=seekerregistration.objects.get(email=email)
                request.session['id']=obj.id
                return render(request, 'seekerhome.html')
            elif(userdetail.keyuser=='JobProvider'):
                print("inside jobprovider")
                email=userdetail.email
                obj=providerregistration.objects.get(email=email)
                request.session['id']=obj.id
                return render(request, 'providerhome.html')
            elif(userdetail.keyuser=='freeLance'):
                email=userdetail.email
                obj=freelanceregistration.objects.get(email=email)
                request.session['id']=obj.id

                return render(request, 'providerhome.html')
            else:          
               # messages.error(request, "Email doesnot exist!!!")
                
                return render(request, 'login.html')
        else:
           # messages.error(request, "Email doesnot exist!!!")
            return render(request, 'login.html',{'form':loginForms})
def viewseekers(request):
    obj=seekerregistration.objects.all()
    return render(request,'viewseeker.html',{'seeker':obj})
def readfile(request,id):
    print (id)
    detail = seekerregistration.objects.values_list('id', 'resume')
    f = open(detail, 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
def providermanagement(request):
    obj=providerregistration.objects.all()
    return render(request,'providermanagement.html',{'provider':obj})
def readfile(request,id):
    print (id)
    detail = providerregistration.objects.values_list('id', 'businesslicense')
    f = open(detail, 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
def approves(request,id):
    providerregistration.objects.filter(id=id).update(status=1)
    obj=providerregistration.objects.all()
    return render (request,'providermanagement.html',{'provider':obj})
def freelance(request):
    obj=freelanceregistration.objects.all()
    return render(request,'freelance.html',{'freelance':obj})
def readfile(request,id):
    print (id)

    detail = freelanceregistration.objects.values_list('id', 'resume')
    f = open(detail, 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
def approvefreelance(request,id):
    print("id=",id)
    freelanceregistration.objects.filter(id=id).update(status=1)
    obj=freelanceregistration.objects.all()
    return render (request,'freelance.html',{'freelance':obj})
def viewfeedback (request):
    id=request.session["id"]
    seeker_feedback=addfeedback.objects.all()
    return render(request,'viewfeedback.html',{'obj':seeker_feedback})
def viewvacancy (request):
    provider_vacancy=vacancy.objects.all()
    return render(request,'vacancymanagement.html',{'obj':provider_vacancy})
def deletestatuss(request,id):
    freelanceregistration.objects.filter(id=id).delete()
    forapprove=freelanceregistration.objects.filter(status=False)
    print("approvefreelance",forapprove)
    approvefreelance=freelanceregistration.objects.filter(status=True)
    print("approved",approvefreelance)
    return render(request,'admin.html',{'forapprove':forapprove,'approvefreelance':approvefreelance})
def deletestatus(request,id):
    providerregistration.objects.filter(id=id).delete()
    forapprove=providerregistration.objects.filter(status=False)
    print("approve",forapprove)
    approves=providerregistration.objects.filter(status=True)
    print("approved",approves)
    return render(request,'admin.html',{'forapprove':forapprove,'approves':approves})
def statusdelete(request,id):
    vacancy.objects.filter(id=id).delete()
    
    return render(request,'admin.html')

