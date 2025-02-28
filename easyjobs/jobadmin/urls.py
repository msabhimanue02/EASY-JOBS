from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
import user .views
urlpatterns = [
    path('',views.index,name=''),
    path('admin',views.admins,name='admin'),
    path('home',user.views.index,name='home'),
    path('logins',views.logins,name='logins'),
    path('seekerregistration',views.seekerregistrations,name='seekerregistration'),
    path('providerregistration',views.providerregistrations,name='providerregistration'),
    path('freelanceregistration',views.freelanceregistrations,name='freelanceregistration'),
    path('viewseekers',views.viewseekers,name='viewseekers'),
    path('readfile/<int:id>',views.readfile,name='readfile'),
    path('providermanagement',views.providermanagement,name='providermanagement'),
    path('readfile/<int:id>',views.readfile,name='readfile'),
    path('approves/<int:id>',views.approves,name='approves'),
    path('freelance',views.freelance,name='freelance'),
    path('readfile/<int:id>',views.readfile,name='readfile'),
    path('approvefreelance/<int:id>',views.approvefreelance,name='approvefreelance'),
    path('viewfeedback',views.viewfeedback,name='viewfeedback'),
    path('viewvacancy',views.viewvacancy,name='viewvacancy'),
    path('deletestatus/<int:id>',views.deletestatuss,name='deletestatus'),
    path('deletestatuss/<int:id>',views.deletestatus,name='deletestatuss'),
    path('statusdelete/<int:id>',views.statusdelete,name='statusdelete'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)