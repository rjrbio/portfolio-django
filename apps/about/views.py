from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import About
from .serializers import AboutSerializer
from apps.techs.models import Technology
from apps.techs.serializers import TechnologySerializer


@api_view(['GET'])
def about(request):
    ctx = {'request': request}
    about_info = About.objects.first()
    technologies = Technology.objects.all()
    return Response({
        'about': AboutSerializer(about_info, context=ctx).data if about_info else None,
        'technologies': TechnologySerializer(technologies, many=True, context=ctx).data,
    })
