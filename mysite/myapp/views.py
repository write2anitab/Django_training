from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.views.generic import View
#                                 ,TemplateView,ListView,DetailView,
#                                 CreateView,DeleteView,
#                                 UpdateView)

import logging
logger = logging.getLogger(__name__)
# Create your views here.
from  .models import Role
from  .models import User
import  json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RoleSerializer,UserSerializer

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

class UserAuthView(View):
   user = authenticate(username="jai", password="password")
   def get(self,request):
       if self.user:
           logger.info('**** User is authentic ****')
           return HttpResponse('User is Authentic !!')
       else:
           logger.info('**** Invalid User / Password ****')
           return HttpResponse('Invalid User / Password ')

#Django API
class RoleView(View):
   def get(self, request):
       roles  = Role.objects.first()
       return HttpResponse(json.dumps(roles.dict_rep()), content_type="text/json")

# DRF View
class RoleDRFView(APIView):
   def get(self, request):
       roles = Role.objects.all()
       serializer = RoleSerializer(roles, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)

   def post(self, request):
       serializer = RoleSerializer(data=request.data)
       res_status = status.HTTP_201_CREATED
       if serializer.is_valid():
           serializer.save()
       else:
           res_status = status.HTTP_400_BAD_REQUEST
       return Response(serializer.data, res_status)

#UserView
class UserDRFView(APIView):
   def get(self, request):
       users = User.objects.all()
       serializer = UserSerializer(users, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)

   def post(self, request):
       serializer = UserSerializer(data=request.data)
       res_status = status.HTTP_201_CREATED
       if serializer.is_valid():
           serializer.save()
       else:
           res_status = status.HTTP_400_BAD_REQUEST
       return Response(serializer.data, res_status)

   def put(self, request):
        id = request.GET.get('id')   # read from query param
        #id = request.data.get('id') # read it from post
        user = User.objects.get(id=id) 
        serializer = UserSerializer(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

   def delete(self, request,format=None):
        id = request.GET.get('id') # read from query param
        user = User.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

