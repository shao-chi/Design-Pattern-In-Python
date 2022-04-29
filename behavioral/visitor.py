from abc import abstractmethod


class VisitorInterface(object):
    @abstractmethod
    def visit_stock(self, stock):
        ...

    @abstractmethod
    def visit_cypto(self, cypto):
        ...


class FinancialInstrumentInterface(object):
    def __init__(self, code, price):
        self._code = code
        self._price = price

    @abstractmethod
    def accept(self, visitor: VisitorInterface):
        ...

    @property
    def code(self):
        return self._code

    @property
    def price(self):
        return self._price


class Stock(FinancialInstrumentInterface):
    def accept(self, visitor: VisitorInterface):
        visitor.visit_stock(self)


class Cypto(FinancialInstrumentInterface):
    def accept(self, visitor: VisitorInterface):
        visitor.visit_cypto(self)


class Sell(VisitorInterface):
    def __init__(self, nums):
        self.nums = nums

    def visit_stock(self, stock):
        total = int(stock.price * self.nums)
        print(f'Sell Stock: {stock.code} * {self.nums} shares (${total}).')

    def visit_cypto(self, cypto):
        total = int(cypto.price * self.nums)
        print(f'Sell Cypto: {cypto.code} * {self.nums} shares (${total}).')


class Buy(VisitorInterface):
    def __init__(self, nums):
        self.nums = nums

    def visit_stock(self, stock):
        total = int(stock.price * self.nums)
        print(f'Buy Stock: {stock.code} * {self.nums} shares (${total}).')

    def visit_cypto(self, cypto):
        total = int(cypto.price * self.nums)
        print(f'Buy Cypto: {cypto.code} * {self.nums} shares (${total}).')


if __name__ == '__main__':
    invests = [
        (Stock('AAPL', 160), Buy(20)),
        (Stock('NVDA', 200), Buy(10)),
        (Cypto('UST', 1), Buy(100)),
        (Stock('TSLA', 1000), Sell(2)),
        (Cypto('BTC', 4000), Sell(1))
    ]

    for item, action in invests:
        item.accept(action)
