from exchange import Exchange
import time
import csv
import os

if not os.path.exists('data'):
    os.makedirs('data')

def save_to_csv(exchange_data):
    with open('data/market_data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([exchange_data['name'], exchange_data['bid'], exchange_data['ask'],
                         exchange_data['bid_vol'], exchange_data['ask_vol'], exchange_data['timestamp']])

def run_simulation(freq=1, run_time_seconds=10):
    exchange1 = Exchange(name="1", bid=100, ask=101, bid_vol=1000, ask_vol=1000, transaction_cost=0.001)
    exchange2 = Exchange(name="2", bid=100.5, ask=101.5, bid_vol=1000, ask_vol=1000, transaction_cost=0.001)
    exchange3 = Exchange(name="3", bid=99.2, ask=101.2, bid_vol=1000, ask_vol=1000, transaction_cost=0.001)
    exchange4 = Exchange(name="4", bid=100.2, ask=100.6, bid_vol=1000, ask_vol=1000, transaction_cost=0.001)

    exchanges = [exchange1, exchange2, exchange3, exchange4]

    with open('data/market_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['exchange', 'bid', 'ask', 'bid_vol', 'ask_vol', 'timestamp'])

    start_time = time.time()

    while time.time() - start_time < run_time_seconds:
        for exchange in exchanges:
            exchange.update_prices()  # Update prices and volumes
            exchange.display_data()  # Display the updated data

            save_to_csv({
                'name': exchange.name,
                'bid': exchange.bid,
                'ask': exchange.ask,
                'bid_vol': exchange.bid_vol,
                'ask_vol': exchange.ask_vol,
                'timestamp': exchange.timestamp
            })
        print("\n")
        time.sleep(freq)  


if __name__ == "__main__":
    run_simulation(freq=1,run_time_seconds=10)
