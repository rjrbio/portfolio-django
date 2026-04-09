from rest_framework import serializers
from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=2, max_length=200, trim_whitespace=True)
    email = serializers.EmailField()
    subject = serializers.CharField(min_length=3, max_length=200, trim_whitespace=True)
    message = serializers.CharField(min_length=10, max_length=5000, trim_whitespace=True)

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

    def validate_message(self, value):
        # Bloquea mensajes de bajo contenido y posibles enlaces de spam.
        lowered = value.lower()
        if "http://" in lowered or "https://" in lowered or "www." in lowered:
            raise serializers.ValidationError("El mensaje no debe incluir enlaces.")
        return value
