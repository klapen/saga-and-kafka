defmodule SagaAndKafka.MixProject do
  use Mix.Project

  def project do
    [
      app: :saga_and_kafka,
      version: "0.1.0",
      elixir: "~> 1.10",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  # Run "mix help compile.app" to learn about applications.
  def application do
    [
      extra_applications: [:logger, :kaffe],
      mod: {SagaAndKafka.Application, []}
    ]
  end

  # Run "mix help deps" to learn about dependencies.
  defp deps do
    [
      {:stream_data, "~> 0.1", only: :test},
      {:sage, "~> 0.4.0"},
      {:kaffe, "~> 1.9"}
    ]
  end
end
