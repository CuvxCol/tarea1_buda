import api.models as models
from rest_framework import serializers

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = ('id', 'name')
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {'required': True}
        }