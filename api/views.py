from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework import generics
from .models import UserAPIModel
from .serializers import UserSerializer
import json
# Create your views here.


class Index(View):

    def get(self, request):
        return HttpResponse('hello')

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        print(data)


class CreateUser(generics.CreateAPIView):
    queryset = UserAPIModel.objects.all()
    serializer_class = UserSerializer

class ListUsers(generics.ListAPIView):
    queryset = UserAPIModel.objects.all()
    serializer_class = UserSerializer