import time
from abc import abstractmethod
from datetime import datetime

from pytz import timezone


class ClientInterface(object):
    '''target'''
    @abstractmethod
    def get_korea_time(self):
        ...


class KoreaTime(object):
    def __init__(self) -> None:
        self.kr_time = datetime.now().astimezone(timezone('Asia/Seoul'))

    def get_korea_time(self):
        return self.kr_time


class TaiwanTime(object):
    '''adaptee / service'''
    def __init__(self) -> None:
        self.tw_time = datetime.now().astimezone(timezone('Asia/Taipei'))

    def get_taiwan_time(self):
        return self.tw_time


class TimeAdapter(ClientInterface):
    def __init__(self, adaptee: TaiwanTime) -> None:
        self.adaptee = adaptee

    def get_korea_time(self):
        tw_time = self.adaptee.get_taiwan_time()
        kr_time = tw_time.astimezone(timezone('Asia/Seoul'))
        return kr_time


if __name__ == '__main__':
    format = "%Y-%m-%d %H:%M:%S %Z%z"

    korea_clock = KoreaTime()
    time.sleep(2)

    taiwan_clock = TaiwanTime()
    time.sleep(2)

    to_korea_adapter = TimeAdapter(taiwan_clock)
    time.sleep(2)

    print('Korea Time:', korea_clock.get_korea_time().strftime(format))
    print('Taiwan Time:', taiwan_clock.get_taiwan_time().strftime(format))
    print('Adapted Time:', to_korea_adapter.get_korea_time().strftime(format))
