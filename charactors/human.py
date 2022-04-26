from states import NormalState


class Human(object):
    def __init__(self, name) -> None:
        self.name = name
        self._job = None
        self._state = NormalState(self)

    def who(method):
        def wrap(self, *args, **kargs):
            print(f"{self.name}:", end=' ')
            method(self, *args, **kargs)
        return wrap

    def introduce(self):
        if self._job:
            job = f"I'm a/an {self._job.name}."
        else:
            job = "I don't have job."
        print(f'''
        My name is {self.name}. {job}
        I feel {self._state.name} now.
        ''')

    @who
    def setJob(self, job):
        self._job = job
        print(f"I become a/an {job.name}.")

    @who
    def work(self):
        if self._job:
            self._state.work()
        else:
            print("I don't have job.")

    @who
    def eat(self):
        self._state.eat()

    @who
    def sleep(self):
        self._state.sleep()

    @who
    def change_state(self, state):
        self._state = state
        print(f"I feel {self._state.name} now.")

    @property
    def job(self):
        return self._job

    @property
    def state(self):
        return self._state
