from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class IndexView(APIView):
    def get(self, request, format=None):
        content = {
          'wmsg': 'Hi'
        }
        return Response(content)
# Create your views here.

