import json
import time

import requests


def get_variables(subject_id):
    url = f'https://bdl.stat.gov.pl/api/v1/variables?subject-id={subject_id}'
    response = requests.get(url)
    data = json.loads(response.content)
    data_normalized = pd.json_normalize(data, record_path='results')

    return data_normalized


def get_data_by_variable(variable_id: str = None, unit_level='5', year='2020'):
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
        time.sleep(1)

    return df


def get_all_data_from_subject(subject_id):
    subject_df = get_variables(subject_id)
    df = pd.DataFrame()

    for variable in subject_df.itertuples():
        variable_df = get_data_by_variable(variable.id)
        variable_df.rename(columns={'val': variable.n1 + ' ' + variable.n2}, inplace=True)

        try:
            variable_df1 = variable_df.iloc[:, [1, 3]]
            df = pd.merge_ordered(df, variable_df1, on='id', how='outer')

        except Exception:
            df = variable_df.iloc[:, [1, 3, 4]]

    return df


def get_multiple_subjects(*subjects):
    for subject in subjects:
