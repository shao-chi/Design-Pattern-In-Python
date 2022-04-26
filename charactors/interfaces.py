from abc import abstractmethod


class StateInterface(object):
    def __init__(self, human) -> None:
        self.human = human

    @abstractmethod
    def work(self):
        self.human.job.work()

    @abstractmethod
    def eat(self):
        print('Eating ...')

    @abstractmethod
    def sleep(self):
        print("Sleeping ...")


class JobInterface(object):
    '''Strategy Pattern'''

    @abstractmethod
    def work(self):
        ...
