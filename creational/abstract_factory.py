from abc import abstractmethod


class Drama(object):
    '''Product 1 Interface'''
    @abstractmethod
    def make(self) -> None:
        ...


class OST(object):
    '''Product 2 Interface'''
    @abstractmethod
    def make(self) -> None:
        ...


class Producer(object):
    '''Abstract Factory Interface'''
    @abstractmethod
    def createDrama(self) -> Drama:
        ...

    @abstractmethod
    def createOST(self) -> OST:
        ...


class RomanticDrama(Drama):
    def make(self) -> None:
        print("Making romantic drama ...")


class RomanticOST(OST):
    def make(self) -> None:
        print("Making romantic OST ...")


class RomanticProducer(Producer):
    def createDrama(self) -> Drama:
        return RomanticDrama()

    def createOST(self) -> OST:
        return RomanticOST()


class FunnyDrama(Drama):
    def make(self) -> None:
        print("Making funny drama ...")


class FunnyOST(OST):
    def make(self) -> None:
        print("Making funny OST ...")


class FunnyProducer(Producer):
    def createDrama(self) -> Drama:
        return FunnyDrama()

    def createOST(self) -> OST:
        return FunnyOST()


class MakingDrama(object):
    def __init__(self, producer: Producer) -> None:
        self.drama = producer.createDrama()
        self.ost = producer.createOST()

    def make(self):
        self.drama.make()
        self.ost.make()


if __name__ == '__main__':
    funny_producer = FunnyProducer()
    romantic_producer = RomanticProducer()

    MakingDrama(funny_producer).make()
    MakingDrama(romantic_producer).make()
