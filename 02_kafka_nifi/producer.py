from kafka import KafkaProducer
import json
from data import get_user
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)


if __name__ == "__main__":
    for i in range(10):
        msg_topic = get_user()
        print(msg_topic)
        producer.send("topic_nifi", msg_topic)
        time.sleep(1)