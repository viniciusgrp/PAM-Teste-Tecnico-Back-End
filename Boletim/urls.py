from django.urls import path
from .views import RelatorioView, CreateRelatorioView, RelatorioAlunoView

urlpatterns = [
    path("relatorios/<int:user_id>/boletim/", CreateRelatorioView.as_view(), name="create-relatorio"),
    path("relatorios/<int:aluno_id>/", RelatorioView.as_view()),
    path("relatorios/<int:aluno_id>/get/", RelatorioAlunoView.as_view()),
]
