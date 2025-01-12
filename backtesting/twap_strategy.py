# backtesting/twap_strategy.py
import random
import sys
from pathlib import Path
project_root = Path.cwd()
exchange_path = project_root / "exchange_simulation"
sys.path.append(str(exchange_path))
from exchange import Exchange

def execute_twap_order(order_qty, exchanges, time_period=10):
    """
    Simulate the execution of a TWAP strategy.
    :param order_qty: The total quantity of the asset to be ordered.
    :param exchanges: A list of exchanges to consider for order execution.
    :param time_period: The duration (in seconds) over which the order is split.
    :return: A dictionary containing the total executed price and other metrics.
    """
    order_chunks = order_qty // time_period  # Split the order evenly across the time period
    executed_price = 0
    executed_qty = 0

    for t in range(time_period):
        # Select the exchange with the best price at this interval (lowest ask price)
        best_exchange = min(exchanges, key=lambda x: x.ask)  # Get the exchange with the lowest ask price
        
        # Simulate executing the order on this exchange
        executed_qty += order_chunks
        executed_price += best_exchange.ask  # Use ask price as executed price

        # Print details for debugging or tracking
        print(f"Executed {order_chunks} units at {best_exchange.ask:.2f} on {best_exchange.name} at time {t+1}")

    avg_executed_price = executed_price / time_period
    return {
        'executed_price': avg_executed_price,
        'executed_qty': executed_qty
    }
