from human import Human
from jobs import Chef
from jobs import Doctor
from jobs import Driver
from jobs import SoftwareEngineer


def main():
    john = Human('John')
    john.setJob(Doctor())
    john.introduce()

    jane = Human('Jane')
    jane.setJob(SoftwareEngineer())
    jane.work()
    jane.introduce()

    john.work()
    john.eat()
    john.sleep()
    john.work()
    john.sleep()
    john.eat()

    jane.eat()
    jane.sleep()
    jane.eat()
    jane.work()

    tom = Human('Tom')
    tom.work()
    tom.eat()
    tom.eat()
    tom.sleep()
    tom.sleep()
    tom.sleep()
    tom.eat()
    tom.setJob(Driver())
    tom.work()

    john.setJob(Chef())
    john.work()
    john.sleep()
    john.work()
    john.eat()
    john.work()


if __name__ == '__main__':
    main()
