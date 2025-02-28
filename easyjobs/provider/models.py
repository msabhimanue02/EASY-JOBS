from django.db import models
import jobadmin.models
class login(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=25)
    keyuser=models.CharField(max_length=30)
class vacancy(models.Model):
    provider_id=models.ForeignKey(jobadmin.models.providerregistration,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    experience=models.IntegerField(max_length=10)
    salary=models.IntegerField()
    vacancies=models.IntegerField()
    def __str__(self):
        return self.names