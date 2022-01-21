class Carteira:

    def __init__(self):
        self.tickers = []
    
    def new_ticker(self, ticker_name, quantidade = 0):
        if not self.find_ticker(ticker_name):
            self.tickers.append({
                "ticker": ticker_name,
                "quantidade": quantidade
            })
        else:
            print("Você já possui esse ticker na carteira.")

    def remove_ticker(self, ticker_name):
        ticker = self.find_ticker(ticker_name)
        if ticker:
            self.tickers.remove(ticker)
        else:
            print("Você não possui esse ticker na carteira.")

    def find_ticker(self, ticker_name):
        for tick in self.tickers:
            if tick.ticker == ticker_name:
                return tick
        return False



