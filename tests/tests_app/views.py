from rest_framework import viewsets
from .models import *


class TestingModelViewset(viewsets.ModelViewSet):
    serializer_class = TestModelSerializer
    queryset = TestingModel.objects.all()


class OneToOneModelViewset(viewsets.ModelViewSet):
    serializer_class = OneToOneTestModelSerializer
    queryset = OneToOneTestModel.objects.all()


class ManyToOneModelViewset(viewsets.ModelViewSet):
    serializer_class = ManyToOneTestModelSerializer
    queryset = ManyToOneTestModel.objects.all()
