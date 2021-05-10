from django.urls import path

from apps.evaluation_folder.views import EvaluationFolderListAPI, EvaluationFolderUpdateAPI, \
    EvaluationFolderRetrieveAPI, EvaluationFolderCreatAPI

urlpatterns = [
    path('list/', EvaluationFolderListAPI.as_view(), name='evaluation_folder_list'),
    path('update/<int:pk>', EvaluationFolderUpdateAPI.as_view(), name='evaluation_folder_update'),
    path('dtaile/<int:pk>', EvaluationFolderRetrieveAPI.as_view(), name='evaluation_folder_detail'),
    path('creat/', EvaluationFolderCreatAPI.as_view(), name='evaluation_folder_creat')
]
