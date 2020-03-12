defmodule EventProducer do
  def send_event({key, value}, topic) do
    Kaffe.Producer.produce_sync(topic, [{key, value}])
  end

  def send_event(key, value) do
    Kaffe.Producer.produce_sync(key, value)
  end
end
