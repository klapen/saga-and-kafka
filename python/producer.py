import sys, getopt
from datetime import datetime
import kafka
from kafka import KafkaProducer

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
            key = arg.encode('utf-8')
        elif opt in ("--value"):
            value = arg

    if not topic or not key or not value:
        print('Error -> Topic, Key and Value are required')
    else:
        try:
            producer = KafkaProducer(bootstrap_servers='localhost:9092')
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            value = "{0} - {1}".format(value,now)
            
            producer.send(topic, key=key, value=value.encode('utf-8')).get()
            print('Message sent.')
            print('Bye!')
        except kafka.errors.NoBrokersAvailable:
            print("Error -> Can't find any Kafka broker on localhost:9092. Please, turn it on")
            sys.exit(2)
