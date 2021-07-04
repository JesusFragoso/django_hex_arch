from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

class UserDetail(RetrieveAPIView):
     def get(self, request, *args, **kwargs):
         return "<h1>Hello!</h1>"