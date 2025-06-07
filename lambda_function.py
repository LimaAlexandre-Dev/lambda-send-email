import boto3
import json

def lambda_handler(event, context):
    ses = boto3.client('ses', region_name="us-east-2")

    try:
        response = ses.send_email(
            Source="seuemail@exemplo.com",
            Destination={
                'ToAddresses': [
                    "destino@exemplo.com"
                ]
            },
            Message={
                'Subject': {
                    'Data': 'Teste de envio via Lambda'
                },
                'Body': {
                    'Text': {
                        'Data': 'Este e-mail foi enviado por uma função Lambda da AWS!'
                    }
                }
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('E-mail enviado com sucesso!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
