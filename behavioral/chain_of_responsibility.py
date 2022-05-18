from abc import abstractmethod


class HandlerInterface(object):
    _next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, handler):
        self._next = handler

    @abstractmethod
    def handle(self, request):
        ...


class Operator(HandlerInterface):
    def __init__(self, value, minimum, maximum) -> None:
        self._value = value
        self._minimum = minimum
        self._maximum = maximum

    def handle(self, result):
        if result > self._maximum:
            print(f'= {result} > {self._maximum}, STOP!')
        elif result < self._minimum:
            print(f'= {result} < {self._minimum}, STOP!')
        else:
            return True
        return False


class Add(Operator):
    def handle(self, result):
        print(f'+ {self._value}', end=' ')
        result += self._value
        if super().handle(result):
            if self._next is None:
                print(f'= {result}')
            else:
                self._next.handle(result)
        else:
            return


class Substract(Operator):
    def handle(self, result):
        print(f'- {self._value}', end=' ')
        result -= self._value
        if super().handle(result):
            if self._next is None:
                print(f'= {result}')
            else:
                self._next.handle(result)
        else:
            return


if __name__ == '__main__':
    add_5 = Add(5, -100, 100)
    add_10 = Add(10, -200, 200)
    sub_20 = Substract(20, -200, 200)

    add_5.next = add_10
    add_10.next = sub_20
    print('0', end=' ')
    add_5.handle(0)

    print('10', end=' ')
    add_10.handle(10)

    print('-195', end=' ')
    add_10.handle(-195)

    print('100', end=' ')
    add_5.handle(100)
