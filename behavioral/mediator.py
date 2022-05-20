from abc import abstractmethod


class MediatorInterface(object):
    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def send(self, sender):
        ...


# Component 1
class User(object):
    def __init__(self, name: str, mediator: MediatorInterface) -> None:
        self._name = name
        self.mediator = mediator

    def send(self, message, receiver=None):
        if receiver is None:
            print(self.name, f'sent "{message}" to everyone')
        else:
            print(self.name, f'sent "{message}" to', receiver.name)
        self.mediator.communicate(message, self, receiver)

    def receive(self, message, sender):
        print(self.name, f'received "{message}" from', sender.name)

    @property
    def name(self):
        return self._name


# Component 2 (Observer)
class Robot(object):
    def __init__(self, name: str, mediator: MediatorInterface) -> None:
        self._name = name
        self.mediator = mediator
        self._subscriber = []

    def add_subscriber(self, user: User):
        self._subscriber.append(user)

    def notify(self, message):
        print(self.name, f'notified "{message}"')
        for user in self._subscriber:
            self.mediator.communicate(message, self, user)

    @property
    def name(self):
        return self._name


class ChatMediator(MediatorInterface):
    def __init__(self) -> None:
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def communicate(self, message, sender, receiver=None):
        if receiver is None:
            # send to everyone
            for user in self.users:
                if user != sender:
                    user.receive(message, sender)
        else:
            receiver.receive(message, sender)


if __name__ == '__main__':
    chat = ChatMediator()

    user_1 = User('John', chat)
    user_2 = User('Jane', chat)
    user_3 = User('Jojo', chat)
    chat.add_user(user_1)
    chat.add_user(user_2)
    chat.add_user(user_3)

    timer = Robot('Timer', chat)
    timer.add_subscriber(user_1)
    timer.add_subscriber(user_2)

    notifier = Robot('Meeting Notifier', chat)
    notifier.add_subscriber(user_2)
    notifier.add_subscriber(user_3)

    timer.notify("It's 18:00.")

    user_1.send("Hi, Jane!", user_2)

    user_2.send("May you .... ?", user_3)

    user_3.send("Hi everyone, Do anyone want some coffee?")

    notifier.notify("The meeting is comming in 10 minutes !!!")
