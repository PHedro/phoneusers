from uuid import uuid4

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from phones.models import Phone
from phones.serializers import PhoneSerializer
from user.models import ConcreteUser


class ConcreteUserSerializer(ModelSerializer):
    phones = PhoneSerializer(many=True)
    name = serializers.CharField(required=True, max_length=30)

    class Meta:
        model = ConcreteUser
        fields = (
            'name',
            'email',
            'password',
            'token',
            'created_at',
            'updated_at',
            'phones'
        )

    def create(self, validated_data):
        phones_data = validated_data.pop('phones', [])
        name = validated_data.pop('name', '')
        splitted = name.split(' ')
        first_name = splitted[0]
        last_name = ' '.join(splitted[1:])
        password_plain = validated_data.pop('password', '')
        _password = make_password(password=password_plain)
        validated_data.update({
            'password': _password,
            'first_name': first_name,
            'last_name': last_name,
        })
        _user = ConcreteUser.objects.create(**validated_data)
        if not _user.token:
            tkn = uuid4()
            while ConcreteUser.objects.filter(token=tkn).exists():
                tkn = uuid4()
            _user.token = tkn
            _user.save()

        for _phone_data in phones_data:
            Phone.objects.create(user=_user, **_phone_data)
        return _user
