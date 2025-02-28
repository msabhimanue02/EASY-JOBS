from django.shortcuts import render
from .models import*
from .forms import*
from provider.models import vacancy
def index (request):
    return render(request,'seekerhome.html')
def base (request):
    return render(request,'seekerhome.html')
def seekerhomes(request):
    return render(request,'seekerhome.html')
""" def logins(request):
    loginform=loginForms()
    return render (request,'login.html',{'form':loginform}) """
""" def addjobseekerfeedback(request):
    if request.method=="GET":
        addfeedback=addfeedbackForm()
        return render(request,'addfeedback.html',{'form':addfeedback})
    else:
        addfeedback=addfeedbackForm(request.POST,request.FILES)
        print("inside post")
        id=request.session["id"]
        if addfeedback.is_valid():
            obj=addfeedback.save(commit=False)
            obj.seeker_id_id=id
            obj.save()
            addfeedback=addfeedbackForm()
        return render(request,'addfeedback.html',{'form':addfeedback})
 """
def sendfeedback(request):
    if request.method=="GET":
        addfeedbackf=addfeedbackForm()
        return render(request,'addfeedback.html',{'form':addfeedbackf})
    else:
        addfeedbackf=addfeedbackForm(request.POST,request.FILES)
        print("inside post")
        id=request.session["id"]
        if addfeedbackf.is_valid():
            obj=addfeedbackf.save(commit=False)
            obj.seeker_id_id=id
            obj.save()
            addfeedbackf=addfeedbackForm()
        return render(request,'addfeedback.html',{'form':addfeedbackf})
    
def viewfeedbackss (request):
    id=request.session["id"]
    seeker_feedback=addfeedback.objects.all()
    return render(request,'viewfeedbacks.html',{'obj':seeker_feedback})    
def vacancyview (request):
    provider_vacancy=vacancy.objects.all()
    return render(request,'viewvacancy.html',{'obj':provider_vacancy})  
def applyforpost(request,id) :
    if applications.objects.filter(vacancy_id_id=id,seeker_id_id=request.session["id"]).exists():
        return render(request,'seekerhome.html')
    else:
        obj=applications(vacancy_id_id=id,seeker_id_id=request.session["id"])
        obj.save()
        return render(request,'seekerhome.html')



    
