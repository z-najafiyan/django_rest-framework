from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from apps.evaluation_folder.models import EvaluationFolder
from apps.evaluation_folder.permissions import ReadonlyPermissions, IsInsurerPermissions, SuperuserPermissions
from apps.evaluation_folder.serializers import EvaluationFolderSerializer


class EvaluationFolderListAPI(ListAPIView):
    queryset = EvaluationFolder.objects.all()
    serializer_class = EvaluationFolderSerializer


class EvaluationFolderCreatAPI(ListCreateAPIView):
    queryset = EvaluationFolder.objects.all()
    serializer_class = EvaluationFolderSerializer
    permission_classes = [IsInsurerPermissions]


class EvaluationFolderUpdateAPI(RetrieveUpdateDestroyAPIView):
    queryset = EvaluationFolder.objects.all()
    serializer_class = EvaluationFolderSerializer
    pagination_class = [IsInsurerPermissions]


class EvaluationFolderRetrieveAPI(RetrieveAPIView):
    queryset = EvaluationFolder.objects.all()
    serializer_class = EvaluationFolderSerializer
