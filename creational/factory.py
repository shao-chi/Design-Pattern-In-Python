import csv
import functools
import os
from abc import abstractmethod
from typing import Callable

import pandas as pd
import pymysql
from pyhive import hive
from TCLIService.ttypes import TOperationState


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
    For DB packages based on Python Database API Specification v2.0
    PEP 249 : https://peps.python.org/pep-0249/
    """
    def __init__(self, connector: Callable, connect_kargs: dict = None):
        self.connector = connector
        self.connect_kargs = connect_kargs

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
    def __init__(self):
        connect_kargs = {
            'host': '0.0.0.0',
            'port': 10001,
            'user': 'client_user',
            'password': 'client_pwd',
            'database': 'products'
        }
        super().__init__(hive.connect, connect_kargs)

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
    def __init__(self):
        connect_kargs = {
            'host': '0.0.0.0',
            'port': 1433,
            'user': 'client_user',
            'password': 'client_pwd',
            'database': 'products'
        }
        super().__init__(pymysql.connect, connect_kargs)


# Creator (Factory)
class Reader(object):
    def read(self, cmd):
        db = self.createDBConnection()
        # ...
        return db.read_date(cmd)

    @abstractmethod
    def createDBConnection(self) -> DBConnectInterface:
        raise NotImplementedError


# Concrete Creator (Concrete Factory)
class HBaseReader(Reader):
    def createDBConnection(self):
        return Hive()


class MySQLReader(Reader):
    def createDBConnection(self):
        return MySQL()


class Application(object):
    def __init__(self):
        self.config = readConfig()
        if self.config['db'] == 'HBase':
            self.reader = HBaseReader()
        elif self.config['db'] == 'MySQL':
            self.reader = MySQLReader()
        else:
            raise "Unknown DB!"

    def main(self):
        self.reader.read(self.config['cmd'])


def readConfig() -> dict:
    ...


if __name__ == '__main__':
    app = Application()
    app.main()
