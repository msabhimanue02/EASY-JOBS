from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
import user .views
urlpatterns = [
    path('seekerhome',views.seekerhomes,name='seekerhome'),
    path('addjobseekerfeedback/<int:id>',views.sendfeedback,name='addjobseekerfeedback'),
#    path('',views.index,name='index'), 
    path('sendfeedback',views.sendfeedback,name='sendfeedback'),
    path('viewfeedbacks',views.viewfeedbackss,name='viewfeedbacks'),
    path('vacancyview',views.vacancyview,name='vacancyview'),
    path('applyforpost/<int:id>',views.applyforpost,name='applyforpost'),
    
    ]
