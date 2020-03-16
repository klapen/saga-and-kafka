# Saga And Kafka

Test to learn about Saga pattern sync with [Kafka](https://kafka.apache.org/), using [Elixir](https://elixir-lang.org/) and [Python 3.8](https://www.python.org/) to consumer/producer.

This project was created following the articles [Sagas Pattern + Property Testing = ❤](https://medium.com/@iacobson/sagas-pattern-property-testing-%EF%B8%8F-fd98aa2ba17b) and [Connecting Elixir to Kafka with Kaffe](https://elixirschool.com/blog/elixir-kaffe-codealong/).

## Dependencies
- Elixir
-- [Kaffe](https://github.com/spreedly/kaffe)
-- [Stream_data](https://github.com/whatyouhide/stream_data)
-- [Sage](https://github.com/Nebo15/sage)
- Python
-- [kafka-python](https://github.com/dpkp/kafka-python)

## Folder struct
```
.
├── docker-compose.yml
├── python
│   ├── consumer.py
│   └── producer.py
├── README.md
└── src
    ├── config
    │   └── config.exs
    ├── mix.exs
    └── test
        ├── saga_and_kafka_test.exs
        └── test_helper.exs

```

## How to use

First of all you need to get a Kafka instance, either on [your local machine](https://kafka.apache.org/quickstart) or using the provided [docker compose](https://docs.docker.com/compose/reference/overview/).

### Python consumer and producer

To use the Python consumer or producer, you need to install [kafka-python](https://github.com/dpkp/kafka-python). It is recommended to use virtual environments for it.

```bash
$ pip install kafka-python
$ cd path/to/saga-and-kafka
$ cd python/plain
$ python consumer.py -t example_topic
```

To test it is working, open a new terminal and send a message with the producer.

```bash
$ cd path/to/saga-and-kafka
$ cd python/plain
$ python producer.py -t example_topic --key=msg_one --value="test value"
```

### Elixir consumer and producer

This simulate a request to order a bike, that requires to order the brakes to complete the order. Brake supplier is a mock that replies out of stock, no response or ordered events.

This request, uses Saga pattern for transactions and compensations. On each of them an event is sent to notify consumer about action performed. By default, the topic is configured to *example_topic* but if you want to chenge it, please change it on config.exs.

To produce events, just run the tests:

```bash
$ cd path/to/saga-and/kafka
$ cd src
$ mix test
```

If you want to see the consumer, open the interactive shell and produce events on a new terminal. To open the interactive shell, type:

```bash
$ cd path/to/saga-and/kafka
$ cd src
$ iex -S mix
```
