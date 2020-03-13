import sys, getopt
from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError

if __name__ == '__main__':
    argv = sys.argv[1:]
    try:
        opts,args = getopt.getopt(argv, "ht:",["topic="])
    except getopt.GetoptError:
        print('consumer.py -t [topic]')
        sys.exit(2)
        
    topic = None
    for opt,arg in opts:
        if opt == '-h':
            print("""
            Connect to a local Kafka stream, on default port, and prints
            recieved messages. To exit press Ctrl + c

            usage: python consummer.py [options]

            Options and arguments:
            -t --topic  : Kafka topic.
            """)
            sys.exit()
        elif opt in ("-t","--topic"):
            topic = arg

    if not topic:
        print('Error -> Topic is required')
    else:
        consumer = None
        try:
            consumer = AvroConsumer({
                'bootstrap.servers': 'localhost:9092',
                'group.id': 'saga-and-kafka',
                'schema.registry.url': 'http://localhost:8081',
                'api.version.request': True})
            consumer.subscribe([topic])
            print('Listening for topic {0} on localhost:9092'.format(topic))
            while True:
                try:
                    msg = consumer.poll(10)
                except SerializerError as e:
                    print('Error -> Message deserialization failed for {}: {}'.format(msg, e))
                    break

                if msg is None:
                    print('No messages to process')
                    continue

                if msg.error():
                    print('Error -> AvroConsumer error: {}'.format(msg.error()))
                    continue

                print ('Event -> {0}: {1}'.format(msg.key(), msg.value()))
        except KeyboardInterrupt:
            print(' Bye!')
            sys.exit()
        except KafkaError as ex:
            print("Error -> Exception on Kafka server (localhost:9092): {0}".format(ex))
            sys.exit(2)
        finally:
            if consumer:
                consumer.close()
