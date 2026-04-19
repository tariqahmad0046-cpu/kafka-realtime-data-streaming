from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Listening...\n")

for message in consumer:
    data = message.value

    # just show summary instead of full image
    print("Received row with", len(data), "pixels")
