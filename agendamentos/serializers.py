from rest_framework import serializers
from .models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

    def to_representation(self, instance):
        # Obtém a representação original dos campos
        representation = super().to_representation(instance)
        
        # Divide por 100 para voltar ao valor original
        valor_pagamento = instance.valor_pagamento / 100

        # Se o valor for inteiro (sem parte decimal), remove a vírgula e zeros
        if valor_pagamento.is_integer():
            representation['valor_pagamento'] = int(valor_pagamento)
        else:
            # Caso contrário, mantém o valor decimal
            representation['valor_pagamento'] = round(valor_pagamento, 2)

        return representation
