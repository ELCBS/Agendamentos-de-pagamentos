from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Agendamento
from .serializers import AgendamentoSerializer

# Criar Agendamento
class AgendamentoCreateView(generics.CreateAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

# Listar Agendamentos
class AgendamentoListView(generics.ListAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

# Consultar Agendamento
class AgendamentoDetailView(generics.RetrieveAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

# Deletar Agendamento (individual)
class AgendamentoDeleteView(generics.DestroyAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

# Deletar Todos os Agendamentos
class AgendamentoDeleteAllView(APIView):
    def delete(self, request, *args, **kwargs):
        # Deleta todos os registros de Agendamento
        Agendamento.objects.all().delete()
        
        # Retorna uma resposta de sucesso
        return Response({"message": "Todos os agendamentos foram deletados."}, status=status.HTTP_204_NO_CONTENT)
