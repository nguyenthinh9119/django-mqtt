from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import *
from .models import ACL

def get_data(data):
    emp= ACL.objects.get(id=data['id'])
    serial = EmpSerializer(emp)
    return serial.data
