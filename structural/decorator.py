from abc import abstractmethod


class CoffeeComponentInterface(object):
    @abstractmethod
    def execute(self):
        ...


class Americano(CoffeeComponentInterface):
    def execute(self):
        print('Making Americano ...')


class Expresso(CoffeeComponentInterface):
    def execute(self):
        print('Making Expresso ...')


class BaseDecorator(CoffeeComponentInterface):
    def __init__(self, coffee: CoffeeComponentInterface):
        self.wrappee = coffee

    def execute(self):
        self.wrappee.execute()


class SugarDecorator(BaseDecorator):
    def execute(self):
        super().execute()
        self.add()

    def add(self):
        print('- Add Sugar.')


class MocaDecorator(BaseDecorator):
    def execute(self):
        super().execute()
        self.add()

    def add(self):
        print('- Add Moca.')


class IceDecorator(BaseDecorator):
    def execute(self):
        super().execute()
        self.add()

    def add(self):
        print('- Add Ice.')


class CreamDecorator(BaseDecorator):
    def execute(self):
        super().execute()
        self.add()

    def add(self):
        print('- Add Cream.')


if __name__ == '__main__':
    cup_1 = Americano()
    cup_1 = IceDecorator(cup_1)
    cup_1 = SugarDecorator(cup_1)
    cup_1 = IceDecorator(cup_1)
    cup_1.execute()

    cup_2 = Expresso()
    cup_2 = SugarDecorator(cup_2)
    cup_2 = CreamDecorator(cup_2)
    cup_2 = MocaDecorator(cup_2)
    cup_2.execute()
