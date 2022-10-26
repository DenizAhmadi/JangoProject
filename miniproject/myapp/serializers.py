from csv import field_size_limit
from rest_framework import serializers
from .models import Deploy, Person

class Login_serializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['username','password']

class Signup_serializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name','username','password']

class addLog_serializer(serializers.ModelSerializer):
    class Meta:
        model = Deploy
        fields = ['deploy_dateTime','description']

class showLog_serializer(serializers.ModelSerializer):
    class Meta:
        model = Deploy
        fields = '__all__'
