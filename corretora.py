import sys
from investidor import Investidor

class Corretora:

    def __init__(self):
        self.investidor = Investidor()
        self.choices = {
            "1": self.show_carteira,
            "2": self.comprar_ticker,
            "3": self.vender_ticker,
            "4": self.quit
        }

    def display_menu(self):
        print("""
        Opções Para Movimentação de Carteira
        
        1. Show all Tickers.
        2. Buy Tickers.
        3. Sell Tickers
        4. Quit
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def show_carteira(self, carteira = None):
        if not carteira:
            carteira = self.investidor.carteira
        for tick in carteira:
            print("{0}: {1}".format(tick.ticker, tick.quantidade))

    def _find_ticker(self, ticker_name):
        for tick in self.investidor.carteira.tickers:
            if tick.ticker == ticker_name:
                return tick
        return False
    
    def comprar_ticker(self):
        ticker_name = input("Enter a ticker name: ")
        quantidade = int(input("Enter a quantidade: "))
        if self._find_ticker(ticker_name):
            tick = self._find_ticker(ticker_name)
            quantidade += tick.quantidade
            self.investidor.carteira.tick = {"ticker": ticker_name, "quantidade": quantidade}
        else:
            self.investidor.carteira.new_ticker(ticker_name, quantidade)

    def vender_ticker(self, ticker_name, quantidade):
        pass

    def quit(self):
        sys.exit(0)

if __name__ == "__main__":
    Corretora().run()