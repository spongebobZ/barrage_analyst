import pymysql
from dbutils.pooled_db import PooledDB
from config.mysql_config import MysqlConf


class ConnectionPool:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.pool = None

    def initialize_pool(self):
        if self.pool is None:
            self.pool = PooledDB(
                creator=pymysql,
                host=MysqlConf.host,
                user=MysqlConf.user,
                password=MysqlConf.password,
                database=MysqlConf.database,
                autocommit=True,
                maxconnections=10
            )

    def get_connection(self):
        self.initialize_pool()
        return self.pool.connection()
