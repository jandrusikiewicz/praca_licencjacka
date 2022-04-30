import json

import pandas as pd
import requests
from azure.storage.blob import BlobClient


def get_variables(subject_id: str) -> pd.DataFrame:
    """Takes subject's ID and returns all variables for this subject.

    Parameters ----------
    subject_id: str
        Subject's ID, for example P3789 for the subject Liczba lokali mieszkalnych
        sprzedanych w ramach transakcji rynkowych (dane kwartalne).

    Returns
    -------
    data_normalized: pd.DataFrame
        Pandas DataFrame containing variables and basic information about them.

    """
    url = f'https://bdl.stat.gov.pl/api/v1/variables?subject-id={subject_id}&page=0&page-size=100'
    response = requests.get(url)
    data = json.loads(response.content)
    data_normalized = pd.json_normalize(data, record_path='results')

    return data_normalized


def get_data_by_variable(variable_id: str = None, unit_level: str = '5', year: str = '2018') -> pd.DataFrame:
    """Takes variable's id, unit's level and year. Returns the data for the selected variable and parameters.

    Parameters
    ----------
    variable_id: str
        ID of the variable, for example 633707.
    unit_level: str
        Territorial units' level. County level is equal to 5.
    year: str
        Year for which we want to get the data.

    Returns
    -------
    df: pd.DataFrame
        Pandas DataFrame containing data from BDL GUS for the selected parameters.

    """
    if variable_id is None:
        variable_id = ''

    url = f'https://bdl.stat.gov.pl/api/v1/data/by-variable/{variable_id}?format=json&unit-level={unit_level}&year={year}&page-size=100'
    url1 = f'https://bdl.stat.gov.pl/api/v1/data/by-variable/{variable_id}?format=json&unit-level={unit_level}&year={year}&page-size=100'
    df = pd.DataFrame()
    counter = 0
    page = 0

    while counter < 1:
        try:
            response = requests.get(url)
            data = json.loads(response.content)
            data_normalized = pd.json_normalize(data['results'], record_path='values', meta=['id', 'name'])
            df = pd.concat([df, data_normalized])

            if url == data['links']['last']:
                counter += 1

        except Exception:
            pass

        page += 1
        url = url1 + '&page=' + str(page)
        # time.sleep(1)

    return df


def get_all_data_from_subject(subject_id: str, unit_level: str = '5', year: str = '2018') -> pd.DataFrame:
    """Gets the data for the all subject's variables and returns as a Pandas DataFrame.

    Parameters
    ----------
    subject_id: str
        Subject's ID, for example P3789 for the subject Liczba lokali mieszkalnych
        sprzedanych w ramach transakcji rynkowych (dane kwartalne).
    unit_level: str
        Territorial units' level. County level is equal to 5.
    year: str
        Year for which we want to get the data.

    Returns
    -------
    df: pd.DataFrame
        Pandas DataFrame containing merged data from BDL GUS for the all variables of the selected subject.

    """
    subject_df = get_variables(subject_id)
    df = pd.DataFrame()

    for variable in subject_df.itertuples():
        variable_df = get_data_by_variable(variable.id, unit_level, year)
        try:
            variable_df.rename(columns={'val': variable.n1 + ' ' + variable.n2 + ' ' + variable.n3}, inplace=True)
        except Exception:  # i zrobi to
            variable_df.rename(columns={'val': variable.n1 + ' ' + variable.n2}, inplace=True)

        try:
            variable_df1 = variable_df.iloc[:, [1, 3]]
            df = pd.merge_ordered(df, variable_df1, on='id', how='outer')

        except Exception:
            df = variable_df.iloc[:, [1, 3, 4]]

    return df


def get_multiple_subjects(subjects_ids: list, unit_level: str, year: str) -> list:
    """Gets data for the multiple subjects.

    Parameters
    ----------
    subjects_ids: list
        List of the subjects' IDs.
    unit_level: str
        Territorial units' level. County level is equal to 5.
    year: str
        Year for which we want to get the data.

    Returns
    -------
    dataframes_list: list
        List of the Pandas Dataframes containing data from BDL GUS for the all selected subjects.

    """
    dataframes_list = []

    for subject in subjects_ids:
        dataframes_list.append(get_all_data_from_subject(subject, unit_level, year))

    return dataframes_list


# def get_container_link(storage_account_name: str, container_name: str) -> str:
#     """Creates a link to the Azure Blob Storage Container.
#
#     Parameters
#     ----------
#     storage_account_name: str
#         Name of the storage account.
#     container_name: str
#         Name of the container.
#
#     Returns
#     -------
#     container_link: str
#
#     """
#     container_link = "wasbs://{0}@{1}.blob.core.windows.net/".format(container_name, storage_account_name)
#
#     return container_link


def get_and_blob(subjects_ids: list, unit_level: int, years: list, tables_names: list, connection_string: str,
                 container_name: str):
    """Get data for the selected parameters and upload to the selected Azure Blob Storage Container.

    Parameters
    ----------
    subjects_ids: list
        List of the subjects' IDs.
    unit_level: int
        Territorial units' level. County level is equal to 5.
    years: list
        List of the years for which we want to het the data.
    tables_names: list
        List of tables' names. Names are related to the subjects' IDs.
    connection_string: str
        Connection String to the Azure Blob Storage.
    container_name: str
        Name of the Azure Blob Storage Container in which we want to save the data.

    """
    unit_level = str(unit_level)
    years = map(str, years)

    for year in years:
        df_list = get_multiple_subjects(subjects_ids, unit_level, year)

        for i, df in enumerate(df_list):
            file = df.to_csv(encoding='UTF-8')

            blob = BlobClient.from_connection_string(
                connection_string,
                container_name=container_name,
                blob_name=year + ' - ' + tables_names[i] + '.csv'
            )

            blob.upload_blob(file)


def get_subject_and_names_lists(filename: str) -> list:  # sprawdz jak zrobic return type gdy zwraca dwie wartosci
    """

    Parameters
    ----------
    filename: str
        Name of the local JSON file containing subjects' IDs and tables' names.

    Returns
    -------
    subjects: list
        List of the subjects' IDs.
    names: list
        List of the tables' names.

    """
    with open(filename) as f:
        table = f.read()

    table = json.loads(table)
    subjects = [*table.keys()]
    names = [*table.values()]

    return subjects, names
