from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle
from .serializers import ContactMessageSerializer


class ContactRateThrottle(AnonRateThrottle):
    scope = 'contact'


@api_view(['POST'])
@throttle_classes([ContactRateThrottle])
def contact(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': '¡Mensaje enviado correctamente!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
