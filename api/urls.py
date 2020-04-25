from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import Index, CreateUser, ListUsers

urlpatterns = [
    url(r'^api/exercise/new-user/?$', CreateUser.as_view()),
    url(r'^api/exercise/users/?$', ListUsers.as_view()),
    url(r'^api/$', Index.as_view()),
]