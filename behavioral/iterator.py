from abc import abstractmethod


class GroupInterface(object):
    @abstractmethod
    def getPhoneNumber(self) -> str:
        ...


class IteratorInterface(object):
    @abstractmethod
    def getNext(self) -> GroupInterface:
        ...

    @abstractmethod
    def hasMore(self) -> bool:
        ...


class WaitingListInterface(object):
    @abstractmethod
    def createIterator(self, group: GroupInterface) -> IteratorInterface:
        ...


class Group(GroupInterface):
    def __init__(self, host, phone_number, num_people):
        self.host = host
        self.phone_number = phone_number
        self.num_people = num_people

    def getPhoneNumber(self) -> str:
        return self.phone_number


class WaitingList(WaitingListInterface):
    line = []

    def add(self, group):
        self.line.append(group)

    def remove(self, remove_group):
        for i, group in enumerate(self.line):
            if group.phone_number == remove_group.phone_number:
                self.line = self.line[:i] + self.line[i+1:]
                break

    def getFirstGroup(self):
        group = self.line[0]
        self.line = self.line[1:]
        return group

    def createIterator(self):
        return Iterator(self)


class Iterator(IteratorInterface):
    def __init__(self,
                 waiting_list: WaitingList,
                 iteration_state: int = -1) -> None:
        self.current_position = iteration_state
        self.waiting_list = waiting_list.line

    def getNext(self) -> GroupInterface:
        if self.hasMore():
            self.current_position += 1
            return self.waiting_list[self.current_position]

    def hasMore(self) -> bool:
        return self.current_position + 1 < len(self.waiting_list)


class RestaurantReception(object):
    def __init__(self):
        print('Start recepting ...\n')
        self.waiting_list = WaitingList()

    def listReservation(self):
        print('List Reservation:')
        iterator = self.waiting_list.createIterator()
        while iterator.hasMore():
            group = iterator.getNext()
            print(group.host, group.phone_number, group.num_people, 'people')
        print('End\n')

    def getReservation(self, group: Group):
        self.waiting_list.add(group)
        print(
            f'Got reservation from {group.host} ({group.num_people} people)\n'
        )

    def checkReservation(self):
        print('Checking reservation ...')
        iterator = self.waiting_list.createIterator()
        while iterator.hasMore():
            group = iterator.getNext()
            self.callCustomer(group)
        print('')

    def cancelReservation(self, group: Group):
        self.waiting_list.remove(group)
        print(
            f'Cancelled reservation from {group.host}\n'
        )

    def callCustomer(self, group: Group):
        print(f'Called {group.host} ({group.phone_number})')


if __name__ == '__main__':
    reception = RestaurantReception()

    group1 = Group('John', '0911111111', 4)
    group2 = Group('Jane', '0922222222', 7)
    group3 = Group('Judy', '0933333333', 2)
    group4 = Group('Tony', '0944444444', 1)
    group5 = Group('Ella', '0955555555', 3)
    group6 = Group('Jins', '0966666666', 4)

    reception.getReservation(group1)
    reception.getReservation(group2)

    reception.listReservation()

    reception.getReservation(group3)
    reception.getReservation(group4)
    reception.getReservation(group5)
    reception.listReservation()

    reception.checkReservation()

    reception.cancelReservation(group4)
    reception.listReservation()

    reception.getReservation(group6)
    reception.cancelReservation(group2)
    reception.listReservation()
