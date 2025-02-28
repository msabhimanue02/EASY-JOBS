from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
import user .views
urlpatterns = [
    path('',views.freelancerhome,name='freelancerhome'),

    ]