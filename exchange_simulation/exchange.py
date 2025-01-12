import random

class SimExchange:
    def __init__(self, name, bid, ask, bid_vol, ask_vol, transaction_cost):
        self.name = name
        self.bid = bid
        self.ask = ask
        self.bid_vol = bid_vol
        self.ask_vol = ask_vol
        self.transaction_cost = transaction_cost
        self.timestamp = 0

    def update_prices(self):
        self.bid += random.uniform(-0.1, 0.1)
        self.ask += random.uniform(-0.1, 0.1)
        
        self.bid_vol += random.randint(-10, 10)
        self.ask_vol += random.randint(-10, 10)

        self.timestamp += 1

    def display_data(self):
        print(f"{self.name} - Bid Price: {self.bid:.2f}, Ask Price: {self.ask:.2f}, "
              f"Bid Volume: {self.bid_vol}, Ask Volume: {self.ask_vol}, "
              f"Transaction Cost: {self.transaction_cost:.4f}, Timestamp: {self.timestamp}")
        

exchange1 = SimExchange(name="Exchange1", bid=100, ask=101, bid_vol=1000, ask_vol=1000, transaction_cost=0.001)
exchange2 = SimExchange(name="Exchange1", bid=100.5, ask=101.5, bid_vol=1000, ask_vol=1000, transaction_cost=0.001)


# Simulating the update process
for _ in range(5):  # Simulating 5 updates
    exchange1.update_prices()
    exchange2.update_prices()
    
    # Display the updated data
    exchange1.display_data()
    exchange2.display_data()


        