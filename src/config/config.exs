use Mix.Config

config :kaffe,
  producer: [
    endpoints: [localhost: 9092],
    # endpoints references [hostname: port]. Kafka is configured to run on port 9092.
    # In this example, the hostname is localhost because we've started the Kafka server
    # straight from our machine. However, if the server is dockerized, the hostname will
    # be called whatever is specified by that container (usually "kafka")
    topics: ["oas_topic"], # add a list of topics you plan to produce messages to
  ]

config :kaffe,
  consumer: [
    endpoints: [localhost: 9092],
    topics: ["oas_topic"],
    consumer_group: "consumer-group",
    message_handler: Consumer,
  ]
