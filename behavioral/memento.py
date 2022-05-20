from copy import deepcopy


class MovingObject(object):
    def __init__(self) -> None:
        self._location = {'x': 0, 'y': 0}

    def move(self, x, y):
        self._location['x'] += x
        self._location['y'] += y
        print(f"Moved. Current Location: {self.location_to_str()}")

    def location_to_str(self):
        return f"({self._location['x']}, {self._location['y']})"

    def __str__(self):
        return f"-- Location: {self.location_to_str()}"

    class Memento(object):
        def __init__(self, location) -> None:
            self._location = location

        def get_state(self):
            return self._location

    def save_memento(self):
        return deepcopy(self.Memento(self._location))

    def resore(self, memento: Memento):
        self._location = memento.get_state()


class CareTaker(object):
    def __init__(self, originator: MovingObject) -> None:
        self._originator = originator
        self._mementos = []

    def save(self):
        self._mementos.append(self._originator.save_memento())
        print('Save state')

    def undo(self):
        memento = self._mementos.pop()
        self._originator.resore(memento)
        print('Undo moving')


if __name__ == '__main__':
    mover = MovingObject()
    caretaker = CareTaker(mover)

    mover.move(2, 4)
    mover.move(-3, 6)
    mover.move(100, -50)
    caretaker.save()

    mover.move(-20, 40)
    mover.move(100, -50)
    caretaker.save()

    mover.move(103, 40)
    mover.move(100, 50)
    caretaker.save()

    mover.move(-33, 3)
    mover.move(12, -50)
    caretaker.save()

    mover.move(12, -50)
    caretaker.undo()
    print(mover)

    caretaker.undo()
    print(mover)

    mover.move(23, 53)
    mover.move(102, -500)
    caretaker.save()

    mover.move(23, 53)
    mover.move(102, -500)
    caretaker.undo()
    print(mover)
