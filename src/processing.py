import pandas as pd
import numpy as np
import logging
from datetime import datetime


def data_processing(csv_paths):

    """
    Process the information from the three .csv files downloaded in order to generate three tables.

    Parameters
    ----------
    csv_paths : list
        list of paths to the .csv files.

    Returns
    -------
    list
        returns a list of the three dataframes created.
    """

    logging.info('Initializing data processing...')
    all_dataframes = []

    museums_df = pd.read_csv(csv_paths[0])
    cinemas_df = pd.read_csv(csv_paths[1])
    libraries_df = pd.read_csv(csv_paths[2])

    # Select data from museums
    m_cols = ["Cod_Loc", "IdProvincia", "IdDepartamento", "categoria", "provincia", "localidad", "nombre", "direccion",
              "CP", "telefono", "Mail", "Web", "fuente"]
    m_sdf = pd.DataFrame(museums_df[m_cols])

    mcols_renamed = {
                     'Cod_Loc': 'cod_localidad',
                     'IdProvincia': 'id_provincia',
                     'IdDepartamento': 'id_departamento',
                     'categoria': 'categoría',
                     'direccion': 'domicilio',
                     'CP': 'código postal',
                     'telefono': 'número de teléfono',
                     'Mail': 'mail',
                     'Web': 'web'
                    }

    m_sdf.rename(columns=mcols_renamed, inplace=True)

    # Select data from cinemas
    c_cols = ["Cod_Loc", "IdProvincia", "IdDepartamento", "Categoría", "Provincia", "Localidad", "Nombre", "Dirección",
              "CP", "Teléfono", "Mail", "Web", "Fuente"]
    c_sdf = pd.DataFrame(cinemas_df[c_cols])

    ccols_renamed = {
                     'Cod_Loc': 'cod_localidad',
                     'IdProvincia': 'id_provincia',
                     'IdDepartamento': 'id_departamento',
                     'Categoría': 'categoría',
                     'Provincia': 'provincia',
                     'Localidad': 'localidad',
                     'Nombre': 'nombre',
                     'Dirección': 'domicilio',
                     'CP': 'código postal',
                     'Teléfono': 'número de teléfono',
                     'Mail': 'mail',
                     'Web': 'web',
                     'Fuente': 'fuente'
                    }

    c_sdf.rename(columns=ccols_renamed, inplace=True)

    # Select data from libraries
    b_cols = ["Cod_Loc", "IdProvincia", "IdDepartamento", "Categoría", "Provincia", "Localidad", "Nombre", "Domicilio",
              "CP", "Teléfono", "Mail", "Web", "Fuente"]
    l_sdf = pd.DataFrame(libraries_df[b_cols])

    lcols_renamed = {
                     'Cod_Loc': 'cod_localidad',
                     'IdProvincia': 'id_provincia',
                     'IdDepartamento': 'id_departamento',
                     'Categoría': 'categoría',
                     'Provincia': 'provincia',
                     'Localidad': 'localidad',
                     'Nombre': 'nombre',
                     'Domicilio': 'domicilio',
                     'CP': 'código postal',
                     'Teléfono': 'número de teléfono',
                     'Mail': 'mail',
                     'Web': 'web',
                     'Fuente': 'fuente'
                    }
    l_sdf.rename(columns=lcols_renamed, inplace=True)

    # Create a single dataframe with the information from all categories
    main_df = pd.concat([m_sdf, c_sdf, l_sdf], axis=0)
    main_df['fecha de carga'] = datetime.now().strftime('%Y-%m-%d')

    # Rename columns' values
    v_renamed = {
                 'Neuquén\xa0': 'Neuquén',
                 'Santa Fé': 'Santa Fe',
                 'Tierra del Fuego': 'Tierra del Fuego, Antártida e Islas del Atlántico Sur',
                 's/d': np.nan
                }
    main_df.replace(v_renamed, inplace=True)

    # Generate dataframe for the first exercise
    fst_df = pd.DataFrame(main_df.drop('fuente', axis='columns'))
    fst_df.reset_index(drop=True, inplace=True)

    all_dataframes.append(fst_df)

    # Generate dataframe for the second exercise

    # Total records per category
    cat_df = main_df.groupby(by="categoría")['mail'].count().reset_index()
    cat_df.rename(columns={'mail': 'total por categoría'}, inplace=True)

    # Total records per source
    source_df = main_df.groupby(by="fuente")['mail'].count().reset_index()
    source_df.rename(columns={'mail': 'total por fuente'}, inplace=True)

    # Records per province and category
    cols = ["provincia", "categoría", "fecha de carga"]
    prov_cat = main_df.groupby(by=cols)['mail'].count().reset_index()
    prov_cat.rename(columns={'mail': 'total por provincia y categoría'}, inplace=True)
    prov_cat = prov_cat[["provincia", "categoría", "total por provincia y categoría", "fecha de carga"]]

    # Join the different information
    snd_df = pd.concat([cat_df, source_df, prov_cat], axis=1)

    all_dataframes.append(snd_df)

    # Generate dataframe for the third exercise

    # Process the required data from cinemas
    cinemas_cols = ['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']
    cinemas_sdf = pd.DataFrame(cinemas_df[cinemas_cols])

    colsc_renamed = {
                     'Pantallas': 'Cantidad de pantallas',
                     'Butacas': 'Cantidad de butacas',
                     'espacio_INCAA': 'Cantidad de espacios INCAA'
                    }
    cinemas_sdf.rename(columns=colsc_renamed, inplace=True)

    # Replace values
    cinemas_sdf.replace({0: np.nan}, inplace=True)

    # Create dataframe
    data = {
            'Cantidad de pantallas': 'sum',
            'Cantidad de butacas': 'sum',
            'Cantidad de espacios INCAA': 'count'
           }
    trd_df = pd.DataFrame(cinemas_sdf.groupby(by='Provincia')[cinemas_sdf.columns].agg(data).reset_index())
    trd_df['fecha de carga'] = datetime.now().strftime('%Y-%m-%d')

    all_dataframes.append(trd_df)

    logging.info('Data processing finished successfully')

    return all_dataframes
