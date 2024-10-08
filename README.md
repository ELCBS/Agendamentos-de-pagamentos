
Projeto desenvolvido com Python e Django para gerenciar agendamentos de pagamentos. Ele permite criar, listar, consultar e excluir agendamentos, armazenando os dados em um banco de dados SQLite. Os dados são retornados e recebidos no formato JSON.


## Funcionalidades

Essa API possui os seguintes endpoints:

1. **Criar Agendamento de Pagamento**
    - **Método**: `POST`
    - **URL**: `/api/agendamentos/`
    - **Descrição**: Cria um novo agendamento de pagamento.
    - **Campos** (JSON):
        - `data_pagamento`: Data no formato `YYYY-MM-DD`.
        - `permite_recorrencia`: Booleano (`true` ou `false`).
        - `quantidade_recorrencia`: Número de recorrências.
        - `intervalo_recorrencia`: Intervalo em dias entre as recorrências.
        - `status_recorrencia`: Status da recorrência (string).
        - `agencia`: Número da agência bancária.
        - `conta`: Número da conta bancária.
        - `valor_pagamento`: Valor do pagamento (decimal, convertido para inteiro no banco de dados).

2. **Listar Todos os Agendamentos**
    - **Método**: `GET`
    - **URL**: `/api/agendamentos/`
    - **Descrição**: Retorna a lista de todos os agendamentos cadastrados.

3. **Consultar Agendamento Específico**
    - **Método**: `GET`
    - **URL**: `/api/agendamentos/<id>/`
    - **Descrição**: Retorna os detalhes de um agendamento específico pelo seu ID.

4. **Deletar Agendamento Específico**
    - **Método**: `DELETE`
    - **URL**: `/api/agendamentos/<id>/`
    - **Descrição**: Exclui um agendamento específico pelo seu ID.

## Linguagem Utilizada 

Python, Django usando o SQLite como banco de dados padrão e Django REST Framework para criação da API


## Pré-requisitos

1º Instalar o Python versão mais recente

2º Instalar o framework django (Comandos: ```pip install django```)

3º instalar o djangorestframework (Comandos: ```pip install djangorestframework```)

## Inicialização

1. Crie o projeto Django:
    ```bash
    django-admin startproject pagamentos
    ```
2. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
3. Acesse o projeto no navegador:
 ```bash
 `http://localhost:8000/`
```
4. Faça download do projeto:

https://github.com/ELCBS/Agendamentos-de-pagamentos/archive/refs/heads/main.zip


## Exemplos de Uso

### Criar um Agendamento de Pagamento

- **Requisição (POST)**:

    ```json
    {
      "data_pagamento": "2024-09-10",
      "permite_recorrencia": true,
      "quantidade_recorrencia": 5,
      "intervalo_recorrencia": 30,
      "status_recorrencia": "ativo",
      "agencia": 1234,
      "conta": 56789,
      "valor_pagamento": 100.50
    }
    ```

- **Resposta**:

    ```json
    {
      "id": 1,
      "data_pagamento": "2024-09-10",
      "permite_recorrencia": true,
      "quantidade_recorrencia": 5,
      "intervalo_recorrencia": 30,
      "status_recorrencia": "ativo",
      "agencia": 1234,
      "conta": 56789,
      "valor_pagamento": 10050
    }
    ```

### Listar Todos os Agendamentos

- **Requisição (GET)**: `http://localhost:8000/api/agendamentos/`

- **Resposta**:

    ```json
    [
      {
        "id": 1,
        "data_pagamento": "2024-09-10",
        "permite_recorrencia": true,
        "quantidade_recorrencia": 5,
        "intervalo_recorrencia": 30,
        "status_recorrencia": "ativo",
        "agencia": 1234,
        "conta": 56789,
        "valor_pagamento": 10050
      },
      ...
    ]
    ```

### Consultar um Agendamento Específico

- **Requisição (GET)**: `http://localhost:8000/api/agendamentos/1/`

- **Resposta**:

    ```json
    {
      "id": 1,
      "data_pagamento": "2024-09-10",
      "permite_recorrencia": true,
      "quantidade_recorrencia": 5,
      "intervalo_recorrencia": 30,
      "status_recorrencia": "ativo",
      "agencia": 1234,
      "conta": 56789,
      "valor_pagamento": 10050
    }
    ```

### Deletar um Agendamento

- **Requisição (DELETE)**: `http://localhost:8000/api/agendamentos/1/`

- **Resposta**: `204 No Content`

## Testes

Você pode testar a API usando ferramentas como **Postman**, **Insomnia**, ou **cURL**.

## Coleção do Postman

Realize o download da coleção de testes no Postman: [Agendamento.postman_collection.json](Agendamento.postman_collection.json)

## Bonus

Acresentado a função para deletar todos os agendamentos para facilitar a limpeza do banco

#Realizado o import no arquivo urls.py 
```bash
AgendamentoDeleteAllView
 ```

Acrescentado:  

```bash
path('agendamentos/delete-all/', AgendamentoDeleteAllView.as_view(), name='agendamento-delete-all')
 ```
     
#No aquivo views.py 

Realizado o import:
```bash
from rest_framework.response import Response
from rest_framework.views import APIView
 ```
E acrescentado a classe:

## Deletar Todos os Agendamentos:
```bash
class AgendamentoDeleteAllView(APIView):
    def delete(self, request, *args, **kwargs):
        # Deleta todos os registros de Agendamento
        Agendamento.objects.all().delete()
 ```
    # Retorna uma resposta de sucesso
    return Response({"message": "Todos os agendamentos foram deletados."}, status=status.HTTP_204_NO_CONTENT)

# Deletar Todos os Agendamentos

- **Requisição (DELETE)**: `http://localhost:8000/api/agendamentos/delete-all/`

- **Resposta**: `message": "Todos os agendamentos foram deletados (204 No Content)`

