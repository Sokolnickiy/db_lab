import psycopg2
from typing import Any
from psycopg2.extras import DictCursor
from db import queries
from db.models import CleanData
from utils.singleton import Singleton
from psycopg2.extensions import QueryCanceledError, connection
from loguru import logger


class DataProducer(Singleton):
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

    def __execute(
        self,
        query: str,
        values: dict[str, Any],
        cursor: DictCursor
    ) -> int | None:
        cursor.execute(
            query=query,
            vars=values
        )
        row = cursor.fetchone()
        return row.get("id") if row else None

    def insert_data(self, clean_data: CleanData):
        with self.__conn.cursor(cursor_factory=DictCursor) as cursor:
            person_id = self.__create_person(
                clean_data=clean_data,
                cursor=cursor
            )
            test_ids = self.__create_tests(
                clean_data=clean_data,
                cursor=cursor
            )
            self.__create_person_tests(
                person_id=person_id,
                test_ids=test_ids,
                cursor=cursor
            )
            self.__conn.commit()

    def __create_e_o(self, clean_data: CleanData, cursor: DictCursor) -> int | None:
        if not clean_data.e_o:
            return None 
        if not clean_data.e_o.location_info:
            location_info_id = None
        else:
            location_info_id = self.__execute(
                query=queries.GET_LOCATION_ID,
                values=clean_data.e_o.location_info.model_dump(),
                cursor=cursor
            )
            if not location_info_id:
                location_info_id = self.__execute(
                    query=queries.CREATE_LOCATION_INFO,
                    values=clean_data.e_o.location_info.model_dump(),
                    cursor=cursor
                )
        e_o_id = self.__execute(
            query=queries.GET_E_O,
            values={
                "name": clean_data.e_o.name,
                "type_name": clean_data.e_o.type_name,
                "parent": clean_data.e_o.parent,
                "location_info_id": location_info_id
            },
            cursor=cursor
        )
        if not e_o_id:
            e_o_id = self.__execute(
                query=queries.CREATE_E_O,
                values={
                    "name": clean_data.e_o.name,
                    "type_name": clean_data.e_o.type_name,
                    "parent": clean_data.e_o.parent,
                    "location_info_id": location_info_id
                },
                cursor=cursor
            )
        return e_o_id

    def __create_person(self, clean_data: CleanData, cursor: DictCursor) -> int | None:
        if not clean_data.person.location_info:
            location_info_id = None
        else:
            location_info_id = self.__execute(
                query=queries.GET_LOCATION_ID,
                values=clean_data.person.location_info.model_dump(),
                cursor=cursor
            )
            if not location_info_id:
                location_info_id = self.__execute(
                    query=queries.CREATE_LOCATION_INFO,
                    values=clean_data.person.location_info.model_dump(),
                    cursor=cursor
                )
        if not clean_data.person.class_info.lang_name or not clean_data.person.class_info.profile_name:
            class_info_id = None
        else:
            class_info_id = self.__execute(
                query=queries.GET_CLASS_INFO,
                values=clean_data.person.class_info.model_dump(),
                cursor=cursor
            )
            if not class_info_id:
                class_info_id = self.__execute(
                    query=queries.CREATE_CLASS_INFO,
                    values=clean_data.person.class_info.model_dump(),
                    cursor=cursor
                )
        e_o_id = self.__create_e_o(
            clean_data=clean_data,
            cursor=cursor
        )
        person_id = self.__execute(
            query=queries.CREATE_PERSON,
            values={
                "outid": clean_data.person.outid,
                "birth": clean_data.person.birth,
                "sex_type": clean_data.person.sex_type,
                "location_info_id": location_info_id,
                "e_o_id": e_o_id,
                "class_info_id": class_info_id
            },
            cursor=cursor
        )
        return person_id

    def __create_tests(self, clean_data: CleanData, cursor: DictCursor) -> list[int] | None:
        test_ids = []
        for test in clean_data.tests:
            if not test.location_info:
                location_info_id = None
            else:
                location_info_id = self.__execute(
                    query=queries.GET_LOCATION_ID,
                    values=clean_data.person.location_info.model_dump(),
                    cursor=cursor
                )
                if not location_info_id:
                    location_info_id = self.__execute(
                        query=queries.CREATE_LOCATION_INFO,
                        values=test.location_info.model_dump(),
                        cursor=cursor
                    )
            test_id = self.__execute(
                query=queries.CREATE_TEST,
                values={
                    "ball": test.ball,
                    "ball12": test.ball_12,
                    "ball100": test.ball_100,
                    "status": test.status,
                    "name": test.name,
                    "dpa_level": test.dpa_level,
                    "adapt_scale": test.adapt_scale,
                    "location_info_id": location_info_id
                },
                cursor=cursor
            )
            if test_id:
                test_ids.append(test_id)
        return test_ids
            
    def __create_person_tests(self, person_id: int | None, test_ids: list[int] | None, cursor: DictCursor) -> list[int]:
        if not person_id:
            return []
        if not test_ids:
            return []
        person_test_ids = []
        for test_id in test_ids:
            person_test_id = self.__execute(
                query=queries.CREATE_PERSON_TEST,
                values={
                    "test_id": test_id,
                    "person_id": person_id
                },
                cursor=cursor
            )
            person_test_ids.append(person_test_id)
        return person_test_ids

