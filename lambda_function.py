import json
import mercadopago
import os


def lambda_handler(event, context):

    sdk = mercadopago.SDK(os.environ["TEST_TOKEN"])
    # Contiene informacion sobre el pago
    payment_data = {
        "transaction_amount": float(event["transaction_amount"]),
        "token": event["token"],
        "installments": int(event["installments"]),
        "payment_method_id": event["payment_method_id"],
        "payer": {
            "email": event["payer"]["email"],
            "identification": {
                "type": event["payer"]["identification"]["type"],
                "number": event["payer"]["identification"]["number"]
            }
        }
    }
    #Creacion del pago
    payment_response = sdk.payment().create(payment_data)
    payment= payment_response["response"]

    rpta={
        
        "status": payment["status"],
        "status_detail": payment["status_detail"],
        "id": payment["id"],
        
    }
    
    
    return{
        "statusCode": 200,
        "body": json.dumps(rpta),
    }
