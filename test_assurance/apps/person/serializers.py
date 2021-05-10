from rest_framework import serializers

from apps.evaluation_folder.models import EvaluationFolder
from apps.person.models import Insured, Lost


class InsuredSerializer(serializers.ModelSerializer):
    class Meta:
        model= Insured
        fields = '__all__'


class LostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost
        fields = '__all__'