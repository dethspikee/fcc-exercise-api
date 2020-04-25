
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserAPIModel
from .serializers import UserSerializer
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
        try:
            user_id = request.GET['userId']
        except:
            return JsonResponse({
                'userId': 'missing userId'
            })
        try:
            users = UserAPIModel.objects.filter(_id=user_id)
        except ValueError:
            return JsonResponse({
                'userId': 'Provide valid user ID'
            })

        if not users:
            return JsonResponse({
                'username': 'Not found'
            })

        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
        
class CreateUser(generics.CreateAPIView):
    queryset = UserAPIModel.objects.all()
    serializer_class = UserSerializer

class ListUsers(generics.ListAPIView):
    queryset = UserAPIModel.objects.all()
    serializer_class = UserSerializer