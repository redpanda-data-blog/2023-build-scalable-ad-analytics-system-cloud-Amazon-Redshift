import csv
import json
from confluent_kafka import Producer

# Kafka producer configuration
config = {
    'bootstrap.servers': 'localhost:19092',  # Update with your Redpanda server address
    'client.id': 'csv-producer'
}

producer = Producer(config)

topic_name = 'ad-data-csv'  # Update with your topic name

# Define your schema
schema = {
    "type": "struct",
    "fields": [
        {"field": "timestamp", "type": "string"},
        {"field": "ad_id", "type": "string"},
        {"field": "platform", "type": "string"},
        {"field": "event_type", "type": "string"},
        {"field": "impressions", "type": "string"},
        {"field": "clicks", "type": "string"},
        {"field": "age", "type": "string"},
        {"field": "gender", "type": "string"},
        {"field": "location", "type": "string"}
    ]
}
def produce_message(record):
    producer.poll(0)
    message = {
        "schema": schema,
        "payload": record
    }
    producer.produce(topic=topic_name, value=json.dumps(message))
    producer.flush()

def produce_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            produce_message(row)

csv_file_path = 'synthetic_ad_dataset.csv'  # Replace with your CSV file path
produce_from_csv(csv_file_path)
