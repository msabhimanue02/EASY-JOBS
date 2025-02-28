from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
import user .views
urlpatterns = [
    path('providerhome',views.providerhomes,name='providerhome'),
    path('addvacancy/<int:id>',views.addvacancy,name='addvacancy'),
    # path('',views.index,name='index'),
    path('feedbackview',views.feedbackviews,name='feedbackview'),
    path('vacancyrequest',views.vacancyrequest,name='vacancyrequest'),
    path('readfile/<int:id>',views.readfiles,name='readfile'),
    path('vacancyviews',views.vacancyviews,name='vacancyviews'),
    path('deletes/<int:id>',views.deletes,name='deletes'),
    

    ]