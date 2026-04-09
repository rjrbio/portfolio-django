from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Project
from .serializers import ProjectSerializer


@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    serializer = ProjectSerializer(project, context={'request': request})
    return Response(serializer.data)
