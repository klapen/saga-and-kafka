use Mix.Config

config :kaffe,
  producer: [
    endpoints: [localhost: 9092],
    topics: ["example_topic"],
  ]

config :kaffe,
  consumer: [
    endpoints: [localhost: 9092],
    topics: ["example_topic"],
    consumer_group: "consumer-group",
    message_handler: Consumer,
  ]
