import os
from loguru import logger
from db_writer import DbWriter
from csv_parser import CsvParser
from queries import insert_query


if __name__ == "__main__":
    db_writer = DbWriter(
        host=os.environ["POSTGRES_HOST"],
        port=int(os.environ["POSTGRES_PORT"]),
        dbname=os.environ["POSTGRES_DB_NAME"],
        password=os.environ["POSTGRES_PASSWORD"],
        user=os.environ["POSTGRES_USER"]
    ) 
    logger.debug("DbWriter initialized")
    csv_parser = CsvParser()
    csv_parser.parse_to_dict()
    logger.debug("Finished parsing csv")
    for row in csv_parser.df.iloc[1:].values.tolist():
        db_writer.execute(
            query=insert_query,
            values=row
        )
    logger.debug("Finished inserting data into postgres")

    
