from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tickets
from .serializers import TicketSerializer


@api_view(['POST'])
def create_ticket(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True, 'message': 'Ticket created successfully.'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class TicketDisplay():
    queryset = Tickets.objects.all()

