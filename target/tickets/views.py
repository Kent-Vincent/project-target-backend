from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import Tickets
from .serializers import TicketSerializer


class TicketsCreate(generics.CreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        request.data['stage'] = request.data.get('stages_id')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"message": "Ticket created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TicketDisplay():
    queryset = Tickets.objects.all()

