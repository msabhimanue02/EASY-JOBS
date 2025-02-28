from django.db import models
class login(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=25)
    keyuser=models.CharField(max_length=30)
class seekerregistration(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    contact=models.BigIntegerField(max_length=10)
    dob=models.DateField()
    address=models.CharField(max_length=30)
    resume=models.FileField(upload_to='documents/')
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=30)
class providerregistration(models.Model):
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField(max_length=10)
    address=models.CharField(max_length=30)
    businesslicense=models.FileField(upload_to='documents/')
    description=models.CharField(max_length=300)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=30)
    status=models.IntegerField(default=0)
class freelanceregistration(models.Model):
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField(max_length=10)
    address=models.CharField(max_length=30)
    resume=models.FileField(upload_to='documents/')
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=30) 
    status=models.IntegerField(default=False)
 


