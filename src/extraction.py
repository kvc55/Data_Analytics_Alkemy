import requests
import logging
from pathlib import Path
from datetime import datetime


def data_extraction():

    """
    Download three .csv files using its urls and save them locally in a directory called 'Datos'.

    Returns
    -------
    list
        returns a list of paths to the .csv files.
    """

    logging.info('Initializing data extraction...')
    csv_paths = []

    categories_dict = {
                       'museos': "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource"
                                 "/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv",
                       'cines': "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource"
                                "/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv",
                       'bibliotecas': "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f"
                                      "/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv "
                      }
    # Generate the .csv paths
    for category, url in categories_dict.items():
        b_path = Path('/Datos/' + category + datetime.now().strftime('/%y-%m/'))
        f_path = category + datetime.now().strftime('-%d-%m-%y') + '.csv'
        final_path = b_path / f_path

        # Create directory
        b_path.mkdir(parents=True, exist_ok=True)

        r = requests.get(url).content

        # Save .csv files
        with open(final_path, 'wb') as file:
            file.write(r)
            csv_paths.append(final_path)

    logging.info('Data extraction finished successfully')

    return csv_paths
