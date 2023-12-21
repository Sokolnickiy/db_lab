import psycopg2
from singleton import Singleton
from psycopg2.extensions import connection
from loguru import logger


class DbWriter(Singleton):
    
    def __init__(
        self,
        host: str,
        port: int,
        dbname: str,
        password: str,
        user: str
    ) -> None:
        self.__conn = self._open_connection(
            host=host,
            port=port,
            dbname=dbname,
            password=password,
            user=user
        )

    def _open_connection(
        self,
        host: str,
        port: int,
        dbname: str,
        password: str,
        user: str
    ) -> connection:
        while True:
            try:
                return psycopg2.connect(
                    host=host,
                    port=port,
                    dbname=dbname,
                    password=password,
                    user=user
                )
            except psycopg2.DatabaseError as e:
                logger.error(e)

    def _close_connection(self) -> None:
        if self.__conn:
            logger.debug("Closing current connection")
            self.__conn.close()

    def execute(
        self,
        query: str,
        values
    ) -> None:
        with self.__conn.cursor() as cursor:
            try:
                cursor.execute(
                    query=query,
                    vars=values
                )
                self.__conn.commit()
            except psycopg2.Error as e:
                logger.error(e)
