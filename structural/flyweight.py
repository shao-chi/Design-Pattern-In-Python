from abc import ABCMeta
from abc import abstractmethod


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight(key)
            self._flyweights[key] = flyweight
        return flyweight


class Flyweight(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def operation(self, car_type):
        print(f'{self.color} {car_type}')


class ConcreteFlyweight(Flyweight):
    def operation(self, car_type):
        super().operation(car_type)


if __name__ == "__main__":
    flyweight_factory = FlyweightFactory()
    concrete_flyweight = flyweight_factory.get_flyweight("Blue")
    print(id(concrete_flyweight))
    concrete_flyweight.operation('Wish')

    concrete_flyweight = flyweight_factory.get_flyweight("Blue")
    print(id(concrete_flyweight))
    concrete_flyweight.operation('RAV4')

    concrete_flyweight = flyweight_factory.get_flyweight("Red")
    print(id(concrete_flyweight))
    concrete_flyweight.operation('RAV4')

    concrete_flyweight = flyweight_factory.get_flyweight("Red")
    print(id(concrete_flyweight))
    concrete_flyweight.operation('Wish')

    concrete_flyweight = flyweight_factory.get_flyweight("Yellow")
    print(id(concrete_flyweight))
    concrete_flyweight.operation('Wish')
