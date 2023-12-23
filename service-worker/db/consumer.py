from typing import Any
import psycopg2
from psycopg2.extras import DictCursor, DictRow
from utils.singleton import Singleton
from psycopg2.extensions import connection
from loguru import logger


class DataConsumer(Singleton):
    
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
            user=user,
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


    def fetch_one(
        self,
        query: str,
        values: dict[str, Any] | None = None
    ) -> DictRow:
        with self.__conn.cursor(cursor_factory=DictCursor) as cursor:
            try:
                cursor.execute(
                    query=query,
                    vars=values
                )
                row = cursor.fetchone()
                self.__conn.commit()
                return row
            except psycopg2.Error as e:
                logger.error(e)
