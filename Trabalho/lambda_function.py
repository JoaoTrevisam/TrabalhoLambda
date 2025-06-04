import json
import re

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf) 

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

  
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    if digito2 != int(cpf[10]):
        return False

    return True

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"]) if isinstance(event["body"], str) else event["body"]
        cpf = body.get("cpf", "")
        cpf_limpo = re.sub(r'\D', '', cpf)

        if not cpf_limpo:
            return {
                "statusCode": 400,
                "body": json.dumps({"mensagem": "CPF não fornecido"})
            }

        valido = validar_cpf(cpf_limpo)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "cpf": cpf_limpo,
                "valido": valido,
                "mensagem": "CPF válido" if valido else "CPF inválido"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"erro": str(e)})
        }
