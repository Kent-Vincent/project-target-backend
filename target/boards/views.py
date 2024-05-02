from django.shortcuts import render
from .models import Boards
from .serializers import BoardsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

class BoardsCreate(generics.CreateAPIView):
    queryset = Boards.objects.all()
    serializer_class = BoardsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"message": "Boards created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardsDisplay():
    queryset = Boards.objects.all()


