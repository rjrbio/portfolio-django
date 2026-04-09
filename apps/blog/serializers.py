from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'excerpt', 'image', 'created_at', 'updated_at']

    def get_image(self, obj):
        if not obj.image:
            return None
        return obj.image.url


class PostDetailSerializer(PostListSerializer):
    class Meta(PostListSerializer.Meta):
        fields = PostListSerializer.Meta.fields + ['content']
