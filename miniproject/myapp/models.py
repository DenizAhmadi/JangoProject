from pyexpat import model
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10, choices=[('admin','admin'),('user','user')], default='user')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(null=True)
    
class Deploy(models.Model):
    deploy_dateTime = models.DateTimeField(null=True)
    description = models.CharField(max_length=600 , null=True)
    person_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(null=True)

class person_deploy_mapper(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    deploy = models.ForeignKey(Deploy, on_delete=models.CASCADE)
    