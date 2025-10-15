from rest_framework import serializers

from api.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [f.name for f in Patient._meta.get_fields()]