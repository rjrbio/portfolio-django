from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'description', 'image',
            'url', 'github_url', 'technologies', 'featured',
            'created_at', 'updated_at',
        ]

    def get_technologies(self, obj):
        return obj.get_technologies_list()

    def get_image(self, obj):
        if not obj.image:
            return None
        return obj.image.url
