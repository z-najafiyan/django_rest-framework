# Create your views here.
from requests import Response
from rest_framework.generics import get_object_or_404, RetrieveAPIView
from rest_framework.views import APIView

from apps.user.models import Admin, Insurer, AssessorExpert
from apps.user.serializers import AdminSerializer, InsurerSerializer, AssessorExpertSerializer


class ProfileAdmin(RetrieveAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class ProfileInsurer(RetrieveAPIView):
    queryset = Insurer.objects.all()
    serializer_class = InsurerSerializer


class ProfileAssessorExpert(RetrieveAPIView):
    queryset = AssessorExpert.objects.all()
    serializer_class = AssessorExpertSerializer
