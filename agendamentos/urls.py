from django.urls import path
from .views import (
    AgendamentoCreateView, 
    AgendamentoListView, 
    AgendamentoDetailView, 
    AgendamentoDeleteView,
    AgendamentoDeleteAllView
)

urlpatterns = [
    path('agendamentos/', AgendamentoCreateView.as_view(), name='create-agendamento'),
    path('agendamentos/list', AgendamentoListView.as_view(), name='list-agendamento'),
    path('agendamentos/<int:pk>/', AgendamentoDetailView.as_view(), name='detail-agendamento'),
    path('agendamentos/<int:pk>/delete/', AgendamentoDeleteView.as_view(), name='delete-agendamento'),
    path('agendamentos/delete-all/', AgendamentoDeleteAllView.as_view(), name='agendamento-delete-all'),
]