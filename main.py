from src.extraction import *
from src.processing import *
from src.loading import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == '__main__':

    # Try to download, process and upload the information from .csv files, if not, an error is showed
    try:
        logging.info('Initializing process... ')
        csv_paths = data_extraction()
        all_dataframes = data_processing(csv_paths)
        data_loading(all_dataframes)
    except Exception as e:
        logging.error('Something went wrong')
        logging.error(e)
    else:
        logging.info('Process finished successfully')
