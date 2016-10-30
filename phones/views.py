from rest_framework import viewsets

from phones.models import Phone
from phones.serializers import PhoneSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()
