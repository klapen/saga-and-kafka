defmodule SagaAndKafka.Application do
  use Application

  def start(_type, args) do
    import Supervisor.Spec
    children = [
      worker(Kaffe.Consumer, [])
    ]
    opts = [strategy: :one_for_one, name: SagaAndKafka.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
