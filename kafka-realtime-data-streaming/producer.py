from kafka import KafkaProducer
import pandas as pd
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# load your dataset
df = pd.read_csv("dataset.csv")

# send row by row
for index, row in df.iterrows():
    data = row.to_dict()

    producer.send("my-topic", value=data)
    print("Sent:", data)

    time.sleep(1)  # simulate real-time
