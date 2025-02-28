from django.db import models
import jobadmin.models
import provider.models
class login(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=25)
    keyuser=models.CharField(max_length=30)
class addfeedback(models.Model):
    seeker_id=models.ForeignKey(jobadmin.models.seekerregistration,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=300)
class applications(models.Model):
    seeker_id=models.ForeignKey(jobadmin.models.seekerregistration,on_delete=models.CASCADE)
    vacancy_id=models.ForeignKey(provider.models.vacancy,on_delete=models.CASCADE)
 