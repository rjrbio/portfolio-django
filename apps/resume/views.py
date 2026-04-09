from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Education, Experience
from .serializers import EducationSerializer, ExperienceSerializer
from apps.about.models import About
from apps.about.serializers import AboutSerializer


@api_view(['GET'])
def resume(request):
    ctx = {'request': request}
    about = About.objects.first()
    return Response({
        'education': EducationSerializer(Education.objects.all(), many=True, context=ctx).data,
        'experience': ExperienceSerializer(Experience.objects.all(), many=True, context=ctx).data,
        'about': AboutSerializer(about, context=ctx).data if about else None,
    })
