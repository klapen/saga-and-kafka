defmodule Consumer do
  # function to accept Kafka messaged MUST be named "handle_message"
  # MUST accept arguments structured as shown here
  # MUST return :ok
  # Can do anything else within the function with the incoming message

  def handle_message(%{key: key, value: value} = message) do
    IO.inspect(message, label: "****")
    IO.puts("#{key}: #{value}")
    :ok
  end
end
