from kafka import KafkaProducer
import json, time, random
from faker import Faker
import logging

logging.basicConfig(level=logging.INFO)
fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    message = {
        "transaction_id": fake.uuid4(),
        "timestamp": fake.iso8601(),
        "store_id": random.randint(1, 10),
        "product_id": random.randint(100, 999),
        "amount": round(random.uniform(5.0, 500.0), 2)
    }
    producer.send('retail_transactions', message)
    logging.info(f"Produced: {message}")
    time.sleep(1)
