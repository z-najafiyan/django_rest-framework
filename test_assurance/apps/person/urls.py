from django.urls import path

from apps.evaluation_folder.views import EvaluationFolderListAPI
from apps.person.views import CreateInsured, CreateLost

urlpatterns = [
    path('create_insured/', CreateInsured.as_view(), name='create_insured'),
    path('create_lost/', CreateLost.as_view(), name='create_lost')
]
