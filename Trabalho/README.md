# Função AWS Lambda - Validar CPF

Esta função Lambda foi desenvolvida como parte do trabalho da disciplina **Arquitetura em Cloud**.

---

## LINK DA LAMBDA: 

https://r3amuykkp6avw3sdg4idnoikvy0ijjzt.lambda-url.sa-east-1.on.aws/
---

## Sobre o Projeto

Validar um número de CPF recebido como entrada JSON, retornando uma resposta indicando se o CPF é válido ou não.

---

## Linguagem

- **Linguagem:** Python e AWS Lambda

---

## Como funciona

### Entrada

A função espera receber um JSON no corpo do evento com o campo "cpf", contendo o CPF a ser validado.
Exemplo de entrada:

json
{
    "cpf": "529.982.247-25"
}

### Saída

json
{
    "cpf": "52998224725",
    "valido": true,
    "mensagem": "CPF válido"
}
