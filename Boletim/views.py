from .models import Relatorio
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import RelatorioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

class CreateRelatorioView(CreateAPIView):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer

    def perform_create(self, serializer):
        # Obtém o user_id da URL
        user_id = self.kwargs['user_id']
        # Define o user_id como o aluno do relatório
        serializer.save(aluno_id=user_id)

class RelatorioView(RetrieveUpdateDestroyAPIView):
    queryset = Relatorio.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = RelatorioSerializer
    lookup_field = 'aluno_id'

    def perform_update(self, serializer):
        serializer.save()

class RelatorioAlunoView(RetrieveAPIView):
    queryset = Relatorio.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = RelatorioSerializer

    lookup_field = 'aluno_id'

    def get_queryset(self):
        id_aluno = self.kwargs['aluno_id']

        return Relatorio.objects.filter(aluno_id=id_aluno)