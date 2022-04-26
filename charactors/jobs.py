from interfaces import JobInterface


class SoftwareEngineer(JobInterface):
    name = 'software engineer'

    def work(self):
        print("Programming ..., Developing ...")


class Doctor(JobInterface):
    name = 'doctor'

    def work(self):
        print("Doing surgery ... ")


class Chef(JobInterface):
    name = 'chef'

    def work(self):
        print("Cooking ... ")


class Driver(JobInterface):
    name = 'driver'

    def work(self):
        print("Driving ... ")
