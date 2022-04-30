class AccountInterface(object):
    '''Implementation Interface'''
    def __init__(self):
        self.asset = {}

    def list_asset(self):
        for key, value in self.asset.items():
            print(f'{key}: {value}')

    def get_amount(self, key):
        if key in self.asset.keys():
            amount = self.asset[key]
            # print(f'Get {key}: {amount}')
            return amount
        # print(f'No {key}')
        return 0

    def set_amount(self, key, value):
        if value == 0:
            del self.asset[key]
            return
        self.asset[key] = value
        # print(f'Set {key}: {self.asset[key]}')


class StockAccount(AccountInterface):
    '''Abstraction'''

    def list_asset(self):
        print("In stock account ---")
        super().list_asset()
        print("--------------------")

    def get_amount(self, key):
        amount = super().get_amount(key)
        return amount

    def set_amount(self, key, value):
        super().set_amount(key, value)


class CyptoWallet(AccountInterface):
    def list_asset(self):
        print("In cypto wallet ++++")
        super().list_asset()
        print("++++++++++++++++++++")

    def get_amount(self, key):
        amount = super().get_amount(key)
        return amount

    def set_amount(self, key, value):
        super().set_amount(key, value)


class Tracer(object):
    def __init__(self, account) -> None:
        self.account = account

    def sell(self, key, value):
        amount = self.account.get_amount(key)
        if amount >= value:
            amount -= value
            self.account.set_amount(key, amount)
            print(f'*** Sold {key} {value}, remain {amount}')
        else:
            self.account.set_amount(key, 0)
            print(f'*** Just sold {key} {amount}')

    def buy(self, key, value):
        amount = self.account.get_amount(key) + value
        self.account.set_amount(key, amount)
        print(f'*** Buy {key} {value}, remain {amount}')

    def list(self):
        self.account.list_asset()


if __name__ == '__main__':
    stock_tracer = Tracer(StockAccount())
    stock_tracer.buy('AAPL', 2)
    stock_tracer.sell('AAPL', 5)
    stock_tracer.buy('GOOGL', 1)
    stock_tracer.buy('NVDA', 2)
    stock_tracer.buy('GOOGL', 2)
    stock_tracer.list()

    cypto_tracer = Tracer(CyptoWallet())
    cypto_tracer.buy('BTC', 2)
    cypto_tracer.sell('BTC', 5)
    cypto_tracer.buy('UST', 1)
    cypto_tracer.list()
