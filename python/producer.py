import sys, getopt
from datetime import datetime

from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from confluent_kafka import KafkaError

if __name__ == '__main__':
    argv = sys.argv[1:]
    try:
        opts,args = getopt.getopt(argv, "ht:",["key=","value=","topic="])
    except getopt.GetoptError:
        print('producer.py -t [topic] --key="key" --value="value"')
        sys.exit(2)
        
    topic = None
    key = None
    value = None
    resend = None
    for opt,arg in opts:
        if opt == '-h':
            print("""
            Connect to a local Kafka stream, on default port, and sends
            a key and value to a topic.

            usage: python producer.py [options]

            Options and arguments:
            -t --topic  : Kafka topic.
               --key    : Message key.
               --value  : Message value.
            """)
            sys.exit()
        elif opt in ("-t","--topic"):
            topic = arg
        elif opt in ("--key"):
            key = arg
        elif opt in ("--value"):
            value = arg

    if not topic or not key or not value:
        print('Error -> Topic, Key and Value are required')
    else:
        try:
            value_schema = avro.load('../avro/ValueSchema.avsc')
            key_schema = avro.load('../avro/KeySchema.avsc')
            key = key
            
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            value = { 'title': 'Time {0}'.format(now), 'message': value }
            
            avroProducer = AvroProducer({
                'bootstrap.servers': 'localhost:9092',
                'group.id': 'saga-and-kafka',
                'schema.registry.url': 'http://localhost:8081'
            }, default_key_schema=key_schema, default_value_schema=value_schema)

            avroProducer.produce(topic=topic, value=value, key=key, key_schema=key_schema, value_schema=value_schema)
            avroProducer.flush(1)
            print('Message sent. Timestamp = {0}'.format(now))
            print('Bye!')
        except KafkaError as ex:
            print("Error -> Exception on Kafka server (localhost:9092): {0}".format(ex))
            sys.exit(2)
