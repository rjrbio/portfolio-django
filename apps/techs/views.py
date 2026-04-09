from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Technology
from .serializers import TechnologySerializer


@api_view(['GET'])
def tech_list(request):
    techs = Technology.objects.all()
    serializer = TechnologySerializer(techs, many=True, context={'request': request})
    return Response(serializer.data)
