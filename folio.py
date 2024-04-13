import requests
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= quantity:
                self.portfolio[symbol] -= quantity
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]
            else:
                print(f"Insufficient quantity of {symbol} shares in the portfolio.")
        else:
            print("Error: {} is not in the portfolio.".format(symbol))

    def track_performance(self):
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            current_price = self.get_stock_price(symbol)
            if current_price is not None:
                total_value += current_price * quantity
                print(f"{symbol}: {quantity} shares - Current Price: ${current_price:.2f} - Total Value: ${total_value:.2f}")
            else:
                print(f"Failed to fetch data for {symbol}")
        print("Total Portfolio Value: ${:.2f}".format(total_value))

    def get_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            current_price = self.get_stock_price(symbol)
            if current_price is not None:
                total_value += current_price * quantity
        return total_value

    def get_stock_price(self, symbol):
        api_key = 'BTONO6WLZLCFWTX9'  # Get your API key from Alpha Vantage
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'

        response = requests.get(url)
        data = response.json()

        if 'Global Quote' in data:
            return float(data['Global Quote']['05. price'])
        else:
            print(f"Error: Unable to fetch data for {symbol}")
            return None


portfolio = StockPortfolio()


while True:
    print("Enter 'add' to add a stock, 'remove' to remove a stock, or 'track' to track portfolio performance:")
    choice = input().lower()

    if choice == 'add':
        symbol = input("Enter the stock symbol: ")
        quantity = int(input("Enter the quantity: "))
        portfolio.add_stock(symbol, quantity)
    elif choice == 'remove':
        symbol = input("Enter the stock symbol: ")
        shares = int(input("Enter the quantity: "))
        portfolio.remove_stock(symbol, quantity)
    elif choice == 'track':
        portfolio.track_performance()
    else:
        print("Invalid action. Please try again.")
