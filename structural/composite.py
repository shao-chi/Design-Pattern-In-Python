from abc import abstractmethod


class ComponentInterface(object):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def operations(self):
        ...


class Folder(ComponentInterface):
    # Composite
    def __init__(self, name: str):
        super().__init__(name)
        self._files = set()
        print(f"Create {name} folder.")

    def operations(self):
        print(f"Folder: {self.name}")
        for file in self._files:
            print(f"    {file.name}")

    def add(self, file: ComponentInterface):
        print(f"Add {file.name} file in {self.name} folder.")
        self._files.add(file)

    def remove(self, file: ComponentInterface):
        print(f"Remove {file.name} file from {self.name} folder.")
        self._files.discard(file)


class File(ComponentInterface):
    def __init__(self, name: str):
        super().__init__(name)
        print(f"Create {name} file.")

    def operations(self):
        print(f"File: {self.name}")


if __name__ == "__main__":
    folder1 = Folder("folder 1")
    folder2 = Folder("folder 2")
    folder3 = Folder("folder 3")
    folder4 = Folder("folder 4")
    folder5 = Folder("folder 5")

    file1 = File("file 1")
    file2 = File("file 2")
    file3 = File("file 3")
    file4 = File("file 4")
    file5 = File("file 5")

    folder1.add(file1)
    folder1.add(file2)
    folder2.add(folder1)
    folder2.add(file3)
    folder3.add(folder2)
    folder3.add(file4)
    folder4.add(folder3)
    folder5.add(folder4)
    folder5.add(file5)

    folder5.operations()
    folder4.operations()

    folder5.remove(folder4)
    folder5.operations()
