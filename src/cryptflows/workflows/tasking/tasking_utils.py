from __future__ import annotations
from typing import TYPE_CHECKING
import requests
import pika
from rich import print

# producer
async def send_task(task: dict, host: dict) -> None:
    print(f"[green]Sending task: {task} to {host}[/green]")
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host["host"]))
    channel = connection.channel()
    
    channel.queue_declare(queue=task["queue"])
    channel.basic_publish(exchange='', routing_key=task["queue"], body=task["body"])
    print(f"[green]Task sent: {task} to {host}[/green]")
    connection.close()
    
    return


async def callback(ch: pika.adapters.blocking_connection.BlockingChannel, method: pika.spec.Basic.Deliver, properties: pika.spec.BasicProperties, body: bytes) -> None:
    print(f"[green]Received task: {body}[/green]")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    return


async def consume_task(task: dict, host: dict) -> None:
    print(f"[green]Consuming task: {task} from {host}[/green]")
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host["host"]))
    channel = connection.channel()
    channel.basic_consume(queue=task["queue"], on_message_callback=callback)
    channel.start_consuming()
    connection.close()
    
    return


    
