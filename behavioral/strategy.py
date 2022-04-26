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


class DiveIntoWaterStrategy(StrategyInterface):
    def do(self):
        print("↓↓↓ Dive Into Water !!")


class TurnAroundStrategy(StrategyInterface):
    def do(self):
        print("↶↶↶ Turn Around !!")


class Transportation(object):
    def setStrategy(self, strategy: StrategyInterface) -> None:
        self.strategy = strategy

    def doStrategy(self):
        self.strategy.do()


class ElectricCar(Transportation):
    def doStrategy(self):
        print('Using Electric Engine --', end=' ')
        super().doStrategy()


class Submarine(Transportation):
    def doStrategy(self):
        print('On the water ~~~~~~', end=' ')
        super().doStrategy()


if __name__ == '__main__':
    car = Transportation()

    car.setStrategy(GoStraightStrategy())
    car.doStrategy()

    car.setStrategy(TurnLeftStrategy())
    car.doStrategy()

    car.setStrategy(TurnRightStrategy())
    car.doStrategy()

    car.setStrategy(TurnAroundStrategy())
    car.doStrategy()

    e_car = ElectricCar()
    e_car.setStrategy(GoStraightStrategy())
    e_car.doStrategy()
    e_car.doStrategy()

    e_car.setStrategy(TurnAroundStrategy())
    e_car.doStrategy()
    e_car.doStrategy()

    subm = Submarine()
    subm.setStrategy(DiveIntoWaterStrategy())
    subm.doStrategy()
