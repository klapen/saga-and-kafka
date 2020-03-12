import sys, getopt
import kafka
from kafka import KafkaConsumer

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
        try:
            consumer = KafkaConsumer(topic)
            print('Listening for topic {0} on localhost:9092'.format(topic))
            for message in consumer:
                kvp = [x.decode('utf-8') for x in [message.key, message.value]]
                print ('Event -> {0}: {1}'.format(*kvp))
        except KeyboardInterrupt:
            print(' Bye!')
            sys.exit()
        except kafka.errors.NoBrokersAvailable:
            print("Error -> Can't find any Kafka broker on localhost:9092. Please, turn it on")
            sys.exit(2)
