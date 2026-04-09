from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    paginator = PageNumberPagination()
    page = paginator.paginate_queryset(posts, request)
    serializer = PostListSerializer(page, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    serializer = PostDetailSerializer(post, context={'request': request})
    return Response(serializer.data)
