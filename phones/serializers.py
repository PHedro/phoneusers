from rest_framework.serializers import ModelSerializer

from phones.models import Phone


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = Phone
        fields = (
            'ddd',
            'number',
        )
