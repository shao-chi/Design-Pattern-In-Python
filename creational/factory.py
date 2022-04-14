import csv
import functools
import os
from abc import abstractmethod

import pandas as pd
import pymysql
from pyhive import hive
from TCLIService.ttypes import TOperationState
# from typing import Callable


def connection(method):
    @functools.wraps(method)
    def decorator(self, *args, **kargs):
        self.connect()
        result = method(self, *args, **kargs)
        self.disconnect()
        return result
    return decorator


# Product Interface
class DBConnectInterface(object):
    """
    F DB or packages based on Python Database API Specification v2.0
    PEP 249 : https://peps.python.org/pep-0249/
    """
    # def __init__(self, connector: Callable, connect_kargs: dict = None):
    #     self.connector = connector
    #     self.connect_kargs = connect_kargs

    def connect(self):
        self.conn = self.connector(**self.connect_kargs)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.cursor.close()
        self.conn.close()

    def _execute(self, cmd):
        self.cursor.execute(cmd)

    @connection
    def execute(self, cmd: str):
        self._execute(cmd)

    @connection
    def read_data(self, cmd: str):
        self._execute(cmd)
        colnames = [v[0] for v in self.cursor.description]
        return pd.DataFrame(self.cursor.fetchall(), columns=colnames)

    @connection
    def save_data(self, cmd: str, filepath: str):
        if os.path.exists(filepath):
            return
        print(filepath)
        self._execute(cmd)
        colnames = [v[0] for v in self.cursor.description]
        with open(filepath, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(colnames)
            writer.writerows(self.cursor)
        print(f'{filepath} saved')


# Concrete Product
class Hive(DBConnectInterface):
    def __init__(self, connect_kargs: dict = None):
        self.connector = hive.connect
        self.connect_kargs = connect_kargs

    def _execute(self, cmd):
        self.cursor.execute(cmd, async_=True)

        status = self.cursor.poll().operationState
        while status in (TOperationState.INITIALIZED_STATE,
                         TOperationState.RUNNING_STATE):
            # logs = self.cursor.fetch_logs()
            # for message in logs:
            #     logging.info(message)
            # # An asynchronous query can be cancelled at any time with:
            # # cursor.cancel()
            status = self.cursor.poll().operationState


# Concrete Product
class MySQL(DBConnectInterface):
    def __init__(self, connect_kargs: dict = None):
        self.connector = pymysql.connect
        self.connect_kargs = connect_kargs


# Creator (Factory)
class Reader(object):
    def read(self, cmd):
        db = self.createDBConnection()
        # ...
        return db.read_date(cmd)

    @abstractmethod
    def createDBConnection(self, connect_kargs: dict) -> DBConnectInterface:
        raise NotImplementedError


# Concrete Creator (Concrete Factory)
class HBaseReader(Reader):
    def createDBConnection(self, connect_kargs: dict):
        return Hive(connect_kargs)


class MySQLReader(Reader):
    def createDBConnection(self, connect_kargs: dict):
        return MySQL(connect_kargs)


class Application(object):
    def __init__(self):
        self.config = readConfig()
        if self.config['db'] == 'HBase':
            self.reader = HBaseReader(self.config['connect_kargs'])
        elif self.config['db'] == 'MySQL':
            self.reader = MySQLReader(self.config['connect_kargs'])
        else:
            raise "Unknown DB!"

    def main(self):
        self.reader.read(self.config['cmd'])


def readConfig() -> dict:
    ...


if __name__ == '__main__':
    app = Application()
    app.main()
