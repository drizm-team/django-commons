from rest_framework import viewsets
from .models import TestModel, ExplicitTestModelSerializer, AutoTestModelSerializer


class AutoTestModelViewset(viewsets.ModelViewSet):
    serializer_class = AutoTestModelSerializer
    queryset = TestModel.objects.all()


class ExplicitTestModelViewset(viewsets.ModelViewSet):
    serializer_class = ExplicitTestModelSerializer
    queryset = TestModel.objects.all()
