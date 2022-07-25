from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserSerializer
from .models import User

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the auth_app index.")