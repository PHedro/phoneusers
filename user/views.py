from rest_framework import viewsets

from user.models import ConcreteUser
from user.serializers import ConcreteUserSerializer


class ConcreteUserViewSet(viewsets.ModelViewSet):
    serializer_class = ConcreteUserSerializer
    queryset = ConcreteUser.objects.all()
