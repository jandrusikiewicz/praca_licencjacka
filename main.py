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
    # response = requests.get(url)
    # data = json.loads(response.content)
    # data_normalized = pd.json_normalize(data['results'], record_path='values', meta=['id', 'name'])
    # data_normalized.drop(columns=['attrId', 'id'], inplace=True)
    # url = data['links']['next']
    # df = pd.concat([df, data_normalized])

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
            data_normalized.drop(columns=['attrId', 'id'], inplace=True)
            df = pd.concat([df, data_normalized])

            print(data['links']['self'])
            print(counter)
            print(page)

            if url == data['links']['last']:
                counter += 1



        except Exception:
            pass

        page += 1
        url = url1 + '&page=' + str(page)

        time.sleep(1)

    return df


# print(get_variables('P3783'))
print(get_data('633617').head(1000))
