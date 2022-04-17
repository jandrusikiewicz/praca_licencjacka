import json
import time

import pandas as pd
import requests


def get_variables(subject_id):
    url = f'https://bdl.stat.gov.pl/api/v1/variables?subject-id={subject_id}'

    response = requests.get(url)
    data = json.loads(response.content)
    data_normalized = pd.json_normalize(data, record_path='results')

    return data_normalized


def get_data(variable_id, unit_level='5', year='2020', column_name="Data"):
    url = f'https://bdl.stat.gov.pl/api/v1/data/by-variable/{variable_id}?format=json&unit-level={unit_level}&year={year}&page-size=100'
    df = pd.DataFrame()
    response = requests.get(url)
    data = json.loads(response.content)
    data_normalized = pd.json_normalize(data['results'], record_path='values', meta=['id', 'name'])
    data_normalized.drop(columns=['attrId', 'id'], inplace=True)
    url = data['links']['next']
    df = pd.concat([df, data_normalized])

    while data['links']['self'] is not data['links']['last']:
        try:
            response = requests.get(url)
            data = json.loads(response.content)
            data_normalized = pd.json_normalize(data['results'], record_path='values', meta=['id', 'name'])
            data_normalized.drop(columns=['attrId', 'id'], inplace=True)

            url = data['links']['next']

            df = pd.concat([df, data_normalized])
        except Exception:
            pass

        time.sleep(1)

    return df


# print(get_variables('P3783'))
# print(get_data('00009').head(1000))


# dziala!!!!!!
response = requests.get(
    'https://bdl.stat.gov.pl/api/v1/data/by-variable/00009?format=json&year=2004&year=2005&year=2006&page=0&page-size=100')
data = json.loads(response.content)
df = pd.DataFrame()

# data_normalized = pd.json_normalize(data['results'], record_path='values', meta=['id', 'name'])
# data_normalized.drop(columns=['attrId', 'id'], inplace=True)
# url = data['links']['next']
# df = pd.concat([df, data_normalized])
print(data)
