from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView

from apps.evaluation_folder.permissions import IsInsurerPermissions
from apps.person.models import Insured, Lost
from apps.person.serializers import InsuredSerializer, LostSerializer


class CreateInsured(ListCreateAPIView):
    queryset = Insured.objects.all()
    serializer_class = InsuredSerializer
    pagination_class = [IsInsurerPermissions]


class CreateLost(ListCreateAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostSerializer
    pagination_class = [IsInsurerPermissions]

