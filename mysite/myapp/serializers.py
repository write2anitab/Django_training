from rest_framework import serializers
from .models import Role
from django.contrib.auth.models import User

class RoleSerializer(serializers.ModelSerializer):
   class Meta:
       model = Role
       fields = (['name'])

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('username','password','first_name','last_name','email')

