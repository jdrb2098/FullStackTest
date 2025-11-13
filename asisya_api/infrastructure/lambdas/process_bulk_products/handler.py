# infrastructure/lambdas/process_bulk_products/handler.py
import json
import boto3
import os

SQS_QUEUE_URL = os.getenv("BULK_PRODUCTS_QUEUE_URL")  # opcional


def handler(event, context):
    print("Evento recibido:", json.dumps(event))

    # Aquí procesas cada mensaje que llegue de SQS
    for record in event.get("Records", []):
        body = record.get("body")
        print("Procesando:", body)
        # Aquí puedes llamar a tu lógica de creación de productos

    return {"statusCode": 200, "body": json.dumps("Procesado")}
