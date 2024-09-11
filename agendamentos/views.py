from django.shortcuts import render

from rest_framework import generics
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

# Deletar Agendamento
class AgendamentoDeleteView(generics.DestroyAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

