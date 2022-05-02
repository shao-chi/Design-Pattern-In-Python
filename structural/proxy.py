from abc import abstractmethod
from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Student(object):
    name: str
    id: str

    def print(self):
        print(f'Name: {self.name}, id: {self.id}')


class DataManageInterface(object):
    '''Service Interface'''

    @abstractmethod
    def add(self, data: object):
        ...

    @abstractmethod
    def get(self, key: str):
        ...

    @abstractmethod
    def list(self):
        ...


class StudentDataManage(DataManageInterface):
    def __init__(self) -> None:
        self.students = set()

    def list(self):
        return self.students

    def add(self, student: Student):
        self.students.add(student)

    def get(self, key: str):
        for student in self.students:
            if key == student.id:
                return student
        return None

    def get_by_name(self, name: str):
        result = []
        for student in self.students:
            if name == student.name:
                result.append(student)
        return result


class StudentDataManageProxy(DataManageInterface):
    def __init__(self) -> None:
        self.data_manage = StudentDataManage()

    def check_password(self, password):
        if password != 'zxcvbnm':
            print('The password is not correct !')
            return False
        return True

    def list(self, password: str = ''):
        if self.check_password(password=password):
            print('Student List:')
            for student in self.data_manage.list():
                student.print()

    def add(self, student: Student, password: str = ''):
        if self.check_password(password=password):
            if student in self.data_manage.list():
                print('The student already exists !', end=' -- ')
                student.print()
                return
            self.data_manage.add(student=student)

    def get(self, key: str, password: str = ''):
        if self.check_password(password=password):
            student = self.data_manage.get(key)
            if student is not None:
                return student
            print(f'The student (id: {key}) does not exists !')

    def get_by_name(self, name: str, password: str = ''):
        if self.check_password(password=password):
            students = self.data_manage.get_by_name(name)
            if len(students) == 0:
                print(f'The student (name: {name}) does not exists !')
            return students


if __name__ == '__main__':
    proxy = StudentDataManageProxy()
    john = Student('John', '1')
    proxy.add(john, password='zzzzzzz')

    proxy.add(john, password='zxcvbnm')
    proxy.add(Student('Jane', '2'), password='zxcvbnm')
    proxy.add(Student('Judy', '3'), password='zxcvbnm')
    proxy.list(password='zxcvbnm')

    proxy.add(john, password='zxcvbnm')

    proxy.add(Student('John', '4'), password='zxcvbnm')
    proxy.add(Student('John', '5'), password='zxcvbnm')
    proxy.list(password='zxcvbnm')

    student = proxy.get('2', password='zxcvbnm')
    if student is not None:
        print('Get: ', end='')
        student.print()
    student = proxy.get('6', password='zxcvbnm')
    if student is not None:
        print('Get: ', end='')
        student.print()

    students = proxy.get_by_name('John', password='zxcvbnm')
    if len(students) > 0:
        for student in students:
            print('Get: ', end='')
            student.print()
    students = proxy.get_by_name('Tony', password='zxcvbnm')
    if len(students) > 0:
        for student in students:
            print('Get: ', end='')
            student.print()
