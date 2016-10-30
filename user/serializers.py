from rest_framework.serializers import ModelSerializer

from phones.models import Phone
from phones.serializers import PhoneSerializer
from user.models import ConcreteUser


class ConcreteUserSerializer(ModelSerializer):
    phones = PhoneSerializer(many=True)

    class Meta:
        model = ConcreteUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            # 'token',
            'created_at',
            'updated_at',
            'phones'
        )

    def create(self, validated_data):
        phones_data = validated_data.pop('phones')
        _user = ConcreteUser.objects.create(**validated_data)
        for _phone_data in phones_data:
            Phone.objects.create(user=_user, **_phone_data)
        return _user
