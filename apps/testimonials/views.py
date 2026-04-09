from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Testimonial
from .serializers import TestimonialSerializer


@api_view(['GET'])
def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    serializer = TestimonialSerializer(testimonials, many=True, context={'request': request})
    return Response(serializer.data)
