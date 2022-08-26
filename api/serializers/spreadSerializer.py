import api.models as models
from rest_framework import serializers

class SpreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spread
        fields = (
            'market_id',
            'spread',
            'iso_code',
            'createdAt',
        )
        read_only_fields = ('id',)
        extra_kwargs = {
            'market_id': {'required': True},
            'spread': {'required': True}
        }
