from copy import deepcopy


class PrototypeInterface(object):
    name = ''

    def __init__(self, color, gender, weight):
        self.color = color
        self.gender = gender
        self.weight = weight

    def clone(self):
        return deepcopy(self)
        # return copy(self)

    def do(self):
        print(
            f"{self.color}, {self.weight} kg, and {self.gender} {self.type}",
            end=' -- '
        )
        print(f"id: {id(self)}")


class Cat(PrototypeInterface):
    type = 'cat'


class Dog(PrototypeInterface):
    type = 'dog'


class Tiger(PrototypeInterface):
    type = 'lion'


class PrototypeRegistry(object):
    __prototypes = {}

    def add(self, prototype: PrototypeInterface, name: str):
        if name not in self.__prototypes.keys():
            self.__prototypes[name] = prototype
            print(f'Add {name}')
        else:
            print(f'{name} already exists.')

    def get(self, name: str):
        return self.__prototypes[name].clone()


class PrototypeFactory(PrototypeRegistry):
    def __init__(self) -> None:
        self.add(Cat('black', 'female', 3.3), 'cat')
        self.add(Dog('white', 'male', 5), 'dog')
        self.add(Tiger('orange', 'female', 20), 'tiger')

    def get_cat(self) -> PrototypeInterface:
        return self.get('cat')

    def get_dog(self) -> PrototypeInterface:
        return self.get('dog')

    def get_tiger(self) -> PrototypeInterface:
        return self.get('tiger')


if __name__ == '__main__':
    factory = PrototypeFactory()

    factory.get_cat().do()
    factory.get_cat().do()
    factory.get_cat().do()
    factory.get_cat().do()
    factory.get_cat().do()
    factory.get_dog().do()
    factory.get_dog().do()
    factory.get_dog().do()
    factory.get_tiger().do()
    factory.get_tiger().do()
    factory.get_tiger().do()
