from rest_framework import serializers
from Boletim.models import Relatorio
from Users.models import User

class RelatorioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Relatorio
        fields = ["id", "portugues", "matematica", "historia", "geografia", "ciencias", "faltas", "aluno"]
        read_only_fields = ["user","id"]
        depth = 1