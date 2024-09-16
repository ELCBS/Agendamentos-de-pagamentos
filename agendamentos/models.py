from django.db import models
from decimal import Decimal

class Agendamento(models.Model):
    data_pagamento = models.DateField()
    permite_recorrencia = models.BooleanField()
    quantidade_recorrencia = models.IntegerField()
    intervalo_recorrencia = models.IntegerField()
    status_recorrencia = models.CharField(max_length=100)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.FloatField()  # Entrada como float

    def save(self, *args, **kwargs):
        # Multiplica o valor por 100 para salvar como centavos (inteiro)
        if isinstance(self.valor_pagamento, (float, Decimal)):
            self.valor_pagamento = int(Decimal(self.valor_pagamento) * 100)  # Multiplica por 100 e converte para inteiro
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Agendamento {self.id}"
