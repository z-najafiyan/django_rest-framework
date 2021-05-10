from rest_framework import serializers

from apps.evaluation_folder.models import EvaluationFolder


class EvaluationFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationFolder
        fields = '__all__'
