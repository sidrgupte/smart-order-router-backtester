import random

class Exchange:
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

        # print(f"DEBUG: {self.name} Timestamp Updated: {self.timestamp}")

    def display_data(self):
        print(f"{self.name} - Bid: {self.bid:.2f}, Ask: {self.ask:.2f}, Bid Vol: {self.bid_vol}, Ask Vol: {self.ask_vol}, Timestamp: {self.timestamp}")
        




        