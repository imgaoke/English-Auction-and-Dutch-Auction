class DutchStrategy:

    def __init__(self, num_strategies):
        self.num_strategies = num_strategies
        self.remaining_money = 0
        self.num_auctions = 0
        self.remaining_total_money = 0
        self.rounds_count = 0
        self.last_price = 0
        self.last_won = False

    # name of the strategy - make sure it is unique
    def name(self):
        return "Big1 Strategy"

    # name of the author of the strategy
    def author(self):
        return "Ke Gao"

    # number of auctions that will be simulated - called before the first auction
    def set_num_auctions(self, num_auctions):
        self.num_auctions = num_auctions

    # amount of money available for all auctions - called before the first aution
    def set_money(self, money):
        self.remaining_money = money
        self.remaining_total_money = self.remaining_money * self.num_auctions

    # called after winning an aution with the price that was paid for the object
    def won(self, price):
        self.remaining_money -= price
        self.remaining_total_money -= price
        self.last_won = True

    # value of the object for this agent - called before every auction
    def set_value(self, value): 
        self.value = value
        self.rounds_count += 1
        if self.last_won == False:
            self.remaining_total_money -= self.last_price


    # shows interest in the object for the current price, called in each iteration of each aution
    def interested(self, price, active_strats):
        self.last_won = False
        self.last_price = price
        remaining_rounds = self.num_auctions - self.rounds_count
        if_bid = False
        if remaining_rounds != 0:
            remaining_average_budge = self.remaining_money / remaining_rounds
        else:
            remaining_average_budge = self.remaining_money
        
        if price <= remaining_average_budge and price <= self.value and price <= self.remaining_money:
            if_bid = True

        
        return if_bid

class EnglishStrategy:

    def __init__(self, num_strategies):
        self.num_strategies = num_strategies
        self.remaining_money = 0
        self.num_auctions = 0
        self.remaining_total_money = 0
        self.rounds_count = 0
        self.last_price = 0
        self.last_won = False

    # name of the strategy - make sure it is unique
    def name(self):
        return "Big1 Strategy"

    # name of the author of the strategy
    def author(self):
        return "Ke Gao"

    # number of auctions that will be simulated - called before the first auction
    def set_num_auctions(self, num_auctions):
        self.num_auctions = num_auctions

    # amount of money available for all auctions - called before the first aution
    def set_money(self, money):
        self.remaining_money = money
        self.remaining_total_money = self.remaining_money * self.num_auctions

    # called after winning an aution with the price that was paid for the object
    def won(self, price):
        self.remaining_money -= price
        self.remaining_total_money -= price
        self.last_won = True

    # value of the object for this agent - called before every auction
    def set_value(self, value): 
        self.value = value
        self.rounds_count += 1
        if self.last_won == False:
            self.remaining_total_money -= self.last_price


    # shows interest in the object for the current price, called in each iteration of each aution
    def interested(self, price, active_strats):
        self.last_won = False
        self.last_price = price
        remaining_rounds = self.num_auctions - self.rounds_count
        remaining_average_money = self.remaining_total_money / self.num_strategies
        if_bid = False
        
        if active_strats >= self.num_strategies * 0.3 and price <= self.value * 0.5 and price <= self.remaining_money and self.remaining_money > remaining_average_money:
            if_bid = True
        if price <= self.value * 0.3 and price <= self.remaining_money:
            if_bid = True
        if remaining_rounds <= 10 and price <= self.value * 0.95 and price <= self.remaining_money:
            if_bid = True

        
        return if_bid

def strategy_ascending(num_strategies):
    return EnglishStrategy(num_strategies)

def strategy_descending(num_strategies):
    return DutchStrategy(num_strategies)