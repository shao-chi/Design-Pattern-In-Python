from abc import abstractmethod


class StrategyInterface(object):
    @abstractmethod
    def do(self) -> None:
        ...


class GoStraightStrategy(StrategyInterface):
    def do(self):
        print("↑↑↑ Go Straight !!")


class TurnRightStrategy(StrategyInterface):
    def do(self):
        print("→→→ Turn Right !!")


class TurnLeftStrategy(StrategyInterface):
    def do(self):
        print("←←← Turn Left !!")


class TurnAroundStrategy(StrategyInterface):
    def do(self):
        print("↶↶↶ Turn Around !!")


class Car(object):
    def setStrategy(self, strategy: StrategyInterface) -> None:
        self.strategy = strategy

    def doStrategy(self):
        self.strategy.do()


if __name__ == '__main__':
    car = Car()

    car.setStrategy(GoStraightStrategy())
    car.doStrategy()

    car.setStrategy(TurnLeftStrategy())
    car.doStrategy()

    car.setStrategy(TurnRightStrategy())
    car.doStrategy()

    car.setStrategy(TurnAroundStrategy())
    car.doStrategy()
