# Kafka Real-Time Data Streaming Project

## 🚀 Overview
This project demonstrates real-time data streaming using Apache Kafka with Python.

## 🛠 Tech Stack
- Apache Kafka
- Python
- Pandas
- Docker

## 📌 Architecture

CSV Dataset → Python Producer → Kafka Topic → Python Consumer

## ⚙️ Setup Instructions

## 1. Start Kafka

```bash
docker-compose up -d
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run Consumer

```bash
python consumer.py
```

## 4. Run Producer

```bash
python producer.py
```

📸 Output
Real-time streaming of dataset
Data sent row by row to Kafka
Consumer receives live data


🎯 Learning Outcome
Kafka fundamentals
Producer/Consumer model
Real-time data pipeline
