from datetime import datetime
from django.db.models import Prefetch
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserAPIModel, Exercise
from .serializers import UserSerializer, ExerciseSerializer, UserLogSerializer, UserFromSerializer
# Create your views here.


# class Index(generics.ListAPIView):
#     serializer_class = UserSerializer


#     def list(self, request):
#         queryset = self.get_queryset()
#         if len(queryset) > 0:
#             serializer = UserSerializer(queryset, many=True)
#             return Response(serializer.data)
#         else:
#             return JsonResponse({
#                 'userId': 'Not Found'
#             })

#     def get_queryset(self):
#         user_id = self.request.query_params.get('userId')
#         queryset = UserAPIModel.objects.filter(_id=user_id)
#         return queryset

class Index(APIView):

    def get(self, request):
        # try:
        #     user_id = request.GET['userId']
        # except:
        #     return JsonResponse({
        #         'userId': 'missing userId'
        #     })
        # try:
        #     users = UserAPIModel.objects.filter(_id=user_id)
        # except ValueError:
        #     return JsonResponse({
        #         'userId': 'Provide valid user ID'
        #     })

        # if not users:
        #     return JsonResponse({
        #         'username': 'Not found'
        #     })
        
        params = {}

        for key, value in request.GET.items():
            params[key] = value

        if 'userId' in params:
            users = UserAPIModel.objects.filter(_id=params['userId'])
            if 'from' in params:
                exercises = Exercise.objects.filter(date__gt=f'{params["from"]}-01-01')
                users = UserAPIModel.objects.prefetch_related(Prefetch('log', exercises)).filter(_id=params['userId'])
                serializer_from = UserFromSerializer(users, many=True, context={'from': params['from']})
                return JsonResponse(serializer_from.data, safe=False)
        else:
            return JsonResponse({
                'error': 'Missing userId'
            })


        serializer_log = UserLogSerializer(users, many=True)
        return JsonResponse(serializer_log.data, safe=False)
        
class CreateUser(generics.CreateAPIView):
    queryset = UserAPIModel.objects.all()
    serializer_class = UserSerializer

class ListUsers(generics.ListAPIView):
    queryset = UserAPIModel.objects.all()
    serializer_class = UserSerializer

class AddExercise(generics.CreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class DeleteUser(generics.DestroyAPIView):
    queryset = UserAPIModel.objects.all()
    serializer_class = UserSerializer

class DeleteExercise(generics.DestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer