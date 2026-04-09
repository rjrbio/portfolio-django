from rest_framework import serializers
from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'position', 'company', 'content', 'avatar', 'rating', 'created_at']

    def get_avatar(self, obj):
        if not obj.avatar:
            return None
        return obj.avatar.url
