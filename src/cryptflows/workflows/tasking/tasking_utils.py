from __future__ import annotations
from typing import TYPE_CHECKING, Dict
import json
import os
import logging
import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties
from rich import print
from ...configs.config import Config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Utility function to load configuration
def load_config() -> Dict[str, str]:
    return {
        "host": Config.RABBITMQ_HOST,
        "port": Config.RABBITMQ_PASSWORD,
        "user": Config.RABBITMQ_USER,
        "password": Config.RABBITMQ_PASSWORD
    }

# Producer
async def send_task(task: dict, host: dict) -> None:
    logger.info(f"Sending task: {task} to {host}")
    config = load_config()

    try:
        credentials = pika.PlainCredentials(config["user"], config["password"])
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host["host"],
            port=config["port"],
            credentials=credentials
        ))
        channel = connection.channel()

        channel.queue_declare(queue=task["queue"])
        channel.basic_publish(exchange='', routing_key=task["queue"], body=json.dumps(task["body"]))
        logger.info(f"Task sent: {task} to {host}")
        connection.close()
    except pika.exceptions.AMQPError as e:
        logger.error(f"Error sending task: {e}")

async def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes) -> None:
    task = json.loads(body)
    logger.info(f"Received task: {task}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

async def consume_task(task: dict, host: dict) -> None:
    logger.info(f"Consuming task: {task} from {host}")
    config = load_config()

    try:
        credentials = pika.PlainCredentials(config["user"], config["password"])
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host["host"],
            port=config["port"],
            credentials=credentials
        ))
        channel = connection.channel()
        channel.queue_declare(queue=task["queue"])
        channel.basic_consume(queue=task["queue"], on_message_callback=callback)
        logger.info("Starting to consume")
        channel.start_consuming()
    except pika.exceptions.AMQPError as e:
        logger.error(f"Error consuming task: {e}")
    finally:
        if 'connection' in locals() and connection.is_open:
            connection.close()

