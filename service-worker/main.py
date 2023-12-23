import os
from db.consumer import DataConsumer
from db.adapter import DataCleaner
from db.producer import DataProducer
from db import queries
from loguru import logger


if __name__ == "__main__":
    consumer = DataConsumer(
        host=os.environ["POSTGRES_HOST"],
        port=int(os.environ["POSTGRES_PORT"]),
        dbname=os.environ["POSTGRES_DB_NAME"],
        password=os.environ["POSTGRES_PASSWORD"],
        user=os.environ["POSTGRES_USER"]
    ) 
    res = consumer.fetch_one(
        query=queries.GET_NUMBER_OF_ROWS
    )
    logger.debug(f"Result:{res}")
    data_cleaner = DataCleaner()
    data_producer = DataProducer(
        host=os.environ["POSTGRES_HOST"],
        port=int(os.environ["POSTGRES_PORT"]),
        dbname=os.environ["POSTGRES_FINAL_DB_NAME"],
        password=os.environ["POSTGRES_PASSWORD"],
        user=os.environ["POSTGRES_USER"]
    )
    i = 1
    while (i <= res["count"]):
        logger.debug(f"Inserting row_id:{i}")
        row = consumer.fetch_one(
            query=queries.GET_GOD_TABLE_ROW,
            values={"id": i}
        )
        clean_data = data_cleaner.parse_row(
            row=row
        )
        data_producer.insert_data(
            clean_data=clean_data
        )
        i += 1
        logger.debug(f"Success")
        
