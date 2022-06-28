import logging
from sqlalchemy import create_engine
from settings import *


def data_loading(all_dataframes):

    """
    Convert the dataframes into tables and upload them to a database.

    Parameters
    ----------
    all_dataframes : list
        list of dataframes.
    """

    logging.info('Initializing data loading...')
    # Create connection to database
    engine = create_engine(f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    # Create empty tables from .sql file
    engine.execute(open("src/tables.sql", "r", encoding='utf-8-sig').read())

    # Load data
    all_dataframes[0].to_sql('fst_table', con=engine, if_exists='replace', index=False)
    all_dataframes[1].to_sql('snd_table', con=engine, if_exists='replace', index=False)
    all_dataframes[2].to_sql('trd_table', con=engine, if_exists='replace', index=False)

    logging.info('Data loading finished successfully')

    return

