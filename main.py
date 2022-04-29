from azure.storage.blob import BlobClient

from scripts import *

pd.set_option('display.max_columns', None)

code = 'DefaultEndpointsProtocol=https;AccountName=pracalicencjacka;AccountKey=9QH+KN4FHq4/cxy6pCQNXoQmvg1SXaj' \
       '+P8ln3iAj6HBcvB8o3VR0JQMq+Vf6Xb7Ewu+FL9XBcTGQj4tR2TD3tA==;EndpointSuffix=core.windows.net '

# extract danych kwartalnych za 2018-2020
# extract danych kwartalnych za 2018-2020
# extract danych kwartalnych za 2018-2020
# extract danych kwartalnych za 2018-2020

# table_names_kwartalne = [
#     'Liczba lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
#     'Mediana cen za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
#     'Powierzchnia użytkowa lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
#     'Średnia cena lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (P3786) (dane kwartalne)',
#     'Średnia cena za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
#     'Wartość lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)'
# ]
#
# subjects_list_kwartalne = ['P3789', 'P3793', 'P3791', 'P3792', 'P3794', 'P3790']
#
#
# def get_and_load(subjects_list: list, unit_level='5', years=[2020], container_code=code, container='con-gus'):
#
#     unit_level = str(unit_level)
#     subjects_list = map(str, subjects_list)
#
#     for year in years:  # iteracja po latach, żeby dla każdego roku mieć osobny plik
#         #year = str(year)
#         df_list = get_multiple_subjects(subjects_list, unit_level, year)
#         print('year')
#         for i, df in enumerate(df_list):
#             # df.iloc[:, 1].add_prefix(table_names[i])
#             file = df.to_csv(encoding='UTF-8')
#
#             blob = BlobClient.from_connection_string(
#                 container_code,
#                 container_name=container,
#                 blob_name=year + table_names_kwartalne[i] + '.csv'  # tu dodac parametr do funkcji zeby table names bylo lepsze
#             )
#
#             blob.upload_blob(file)
#             print('git')
#
#
# get_and_load(subjects_list_kwartalne, 5, [2018, 2019, 2020], code, 'con-gus-kwartalne')

# extract danych rocznych za 2018-2020
# extract danych rocznych za 2018-2020
# extract danych rocznych za 2018-2020
# extract danych rocznych za 2018-2020
# extract danych rocznych za 2018-2020


table_names = [
    'Liczba lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
    'Mediana cen za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
    'Powierzchnia użytkowa lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
    'Średnia cena lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (P3786)',
    'Średnia cena za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
    'Wartość lokali mieszkalnych sprzedanych w ramach transakcji rynkowych'
]

code = 'DefaultEndpointsProtocol=https;AccountName=pracalicencjacka;AccountKey=9QH+KN4FHq4/cxy6pCQNXoQmvg1SXaj+P8ln3iAj6HBcvB8o3VR0JQMq+Vf6Xb7Ewu+FL9XBcTGQj4tR2TD3tA==;EndpointSuffix=core.windows.net'
years = [2018]
ids = ['P3783', 'P3787', 'P3785', 'P3786', 'P3788', 'P3784']


def get_and_blob(subjects_ids: list, unit_level: int, years: list, connection_string: str, container_name: str):
    unit_level = str(unit_level)
    years = map(str, years)

    for year in years:
        df_list = get_multiple_subjects(subjects_ids, unit_level, year)

        for i, df in enumerate(df_list):
            # df.iloc[:, 1].add_prefix(table_names[i])
            file = df.to_csv(encoding='UTF-8')

            blob = BlobClient.from_connection_string(
                connection_string,
                container_name=container_name,
                blob_name=year + ' ' + table_names[i] + '.csv'
            )

            blob.upload_blob(file)


get_and_blob(ids, 5, years, code, 'con-gus-kwartalne')
