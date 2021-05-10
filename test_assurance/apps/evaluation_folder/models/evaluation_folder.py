from django.db import models


class EvaluationFolder_lost(models.Model):
    lost = models.ForeignKey("person.Lost", on_delete=models.PROTECT)
    evaluation_folder = models.ForeignKey('evaluation_folder.EvaluationFolder', on_delete=models.PROTECT)
    scan_documents_lost = models.FileField(upload_to='documents/scan_documents_lost/%Y/%m/%d/')


class EvaluationFolder(models.Model):
    court_documents = models.FileField(upload_to='documents/court_documents/%Y/%m/%d/')
    scan_documents_insurer = models.FileField(upload_to='documents/scan_documents_insurer/%Y/%m/%d/')
    damage_accident_file = models.FileField(upload_to='documents/damage_accident_file/%Y/%m/%d/')
    guilty = models.ForeignKey("person.Insured", on_delete=models.PROTECT)
    lost = models.ManyToManyField("person.Lost", through='EvaluationFolder_lost')
    assessor_expert = models.ManyToManyField('user.AssessorExpert')
    insurer = models.OneToOneField("user.Insurer",on_delete=models.PROTECT)
