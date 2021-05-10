from rest_framework import serializers

from apps.evaluation_folder.models import EvaluationFolder
from apps.user.models import Admin, Insurer, AssessorExpert


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['first_name', 'last_name', 'phone_number']


class InsurerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurer
        fields = ['insurer_number', 'established_year', 'name']


class AssessorExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessorExpert
        fields = ['first_name', 'last_name', 'phone_number', 'work_experience_years']
