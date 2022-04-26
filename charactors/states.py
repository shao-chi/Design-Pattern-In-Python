from interfaces import StateInterface


class NormalState(StateInterface):
    name = 'normal'

    def work(self):
        super().work()
        self.human.change_state(TiredState(self.human))

    def eat(self):
        super().eat()

    def sleep(self):
        super().sleep()
        self.human.change_state(HungryState(self.human))


class TiredState(StateInterface):
    name = 'tired'

    def work(self):
        print("I'm tired ... ")

    def eat(self):
        super().eat()
        print("      I need sleeping !!! ")

    def sleep(self):
        super().sleep()
        self.human.change_state(HungryState(self.human))


class HungryState(StateInterface):
    name = 'hungry'

    def work(self):
        print("I'm too hungry to work ... ")

    def eat(self):
        super().eat()
        self.human.change_state(NormalState(self.human))

    def sleep(self):
        print("Let me eat !!! ")
