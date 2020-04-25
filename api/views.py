from django.core.serializers import serialize


from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .models import UserAPIModel
from .serializers import UserSerializer
import json
# Create your views here.


class Index(View):

    def get(self, request):
        try:
            user_id = request.GET['userId']
        except:
            return JsonResponse({
                'userId': 'Missing value'
            })
        user = UserAPIModel.objects.get(_id=user_id)
        exercises = serialize('json', user.exercises.all())
        print(exercises[0])
        return JsonResponse({
            '_id': user._id,
            'username': user.username,
            'count': len(user.exercises.all())
        })
        

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        print(data)


class CreateUser(generics.CreateAPIView):
    queryset = UserAPIModel.objects.all()
    serializer_class = UserSerializer

class ListUsers(generics.ListAPIView):
    queryset = UserAPIModel.objects.all()
    serializer_class = UserSerializer