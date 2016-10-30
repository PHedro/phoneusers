from rest_framework.serializers import ModelSerializer

from user.models import ConcreteUser


class ConcreteUserSerializer(ModelSerializer):
    class Meta:
        model = ConcreteUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'token',
            'created_at',
            'updated_at'
        )
