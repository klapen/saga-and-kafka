defmodule SagaAndKafka do
  require Logger

  alias Mock.{BrakesSupplier}

  def order_bike({brakes_pid}) do
    Sage.new()
    |> Sage.run(:brakes, &brakes_transaction/2, &brakes_compensation/4)
    |> Sage.execute(%{bike_order: self(), brakes_pid: brakes_pid})
  end

  defp brakes_transaction(
    _effects_so_far,
    %{brakes_pid: brakes_pid}
  ) do
    EventProducer.send_event({"order.create", "Waiting for confirmation " <> "#{DateTime.utc_now}"}, "oas_topic")
    BrakesSupplier.order(brakes_pid)
  end

  defp brakes_compensation(
    _effect_to_compensate,
    _effects_so_far,
    {:brakes, {:brakes, :no_response}},
    _attrs
  ) do
    {:retry, retry_limit: 2}
  end

  defp brakes_compensation(
    _effect_to_compensate,
    _effects_so_far,
    _error,
    _attrs
  ) do
    :ok
  end
end
