class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        self._id = id(self)

    def print_id(self) -> None:
        print("id:", self._id)


class NonSingleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self) -> None:
        self._id = id(self)

    def print_id(self) -> None:
        print("id:", self._id)


if __name__ == '__main__':
    singleton_1 = Singleton()
    print(f"{singleton_1=}, ", end='')
    singleton_1.print_id()

    singleton_2 = Singleton()
    print(f"{singleton_2=}, ", end='')
    singleton_2.print_id()

    non_1 = NonSingleton()
    print(f"{non_1=}, ", end='')
    non_1.print_id()

    non_2 = NonSingleton()
    print(f"{non_2=}, ", end='')
    non_2.print_id()

    singleton_3 = Singleton()
    print(f"{singleton_3=}, ", end='')
    singleton_3.print_id()

    non_2 = NonSingleton()
    print(f"{non_2=}, ", end='')
    non_2.print_id()
