from django.db import models

class Relatorio(models.Model):
    portugues = models.PositiveIntegerField()
    matematica = models.PositiveIntegerField()
    historia = models.PositiveIntegerField()
    geografia = models.PositiveIntegerField()
    ciencias = models.PositiveIntegerField()
    faltas = models.PositiveIntegerField()
    aluno = models.OneToOneField("Users.User", on_delete=models.CASCADE)