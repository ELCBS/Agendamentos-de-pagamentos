from rest_framework import serializers
from .models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

    def to_representation(self, instance):
        # Usa o método padrão para pegar a representação
        representation = super().to_representation(instance)

        # Remove o ponto final caso o valor seja um número inteiro
        valor_pagamento = representation.get('valor_pagamento', None)
        if valor_pagamento is not None:
            # Verifica se o valor é float e o converte para int para remover o ponto decimal
            representation['valor_pagamento'] = int(valor_pagamento)
        
        return representation
