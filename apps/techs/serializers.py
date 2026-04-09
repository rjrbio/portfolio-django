from rest_framework import serializers
from .models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = Technology
        fields = ['id', 'name', 'icon', 'icon_class', 'proficiency', 'category']

    def get_icon(self, obj):
        if not obj.icon:
            return None
        return obj.icon.url
