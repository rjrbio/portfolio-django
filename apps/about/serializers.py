from rest_framework import serializers
from .models import About


class AboutSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()
    cv_file = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = [
            'id', 'name', 'title', 'bio', 'profile_image',
            'email', 'phone', 'location',
            'github', 'linkedin', 'twitter', 'cv_file',
        ]

    def get_profile_image(self, obj):
        if not obj.profile_image:
            return None
        return obj.profile_image.url

    def get_cv_file(self, obj):
        if not obj.cv_file:
            return None
        return obj.cv_file.url
