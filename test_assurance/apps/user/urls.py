from django.urls import path
from apps.user.views import ProfileInsurer, ProfileAdmin, ProfileAssessorExpert

urlpatterns = [
    path('profile_admin/<int:pk>', ProfileAdmin.as_view(), name='profile_admin'),
    path('profiel_insurer/<int:pk>', ProfileInsurer.as_view(), name='profile_insurer'),
    path('profile_assessorexpert/<int:pk>', ProfileAssessorExpert.as_view(), name='profile_assessor_expert'),
]
