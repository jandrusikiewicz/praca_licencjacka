from scripts import *

pd.set_option('display.max_columns', None)

print(get_variables('P3783').to_string())
# # print(get_data_by_variable('633617').head(1000))
# df_list = get_multiple_subjects('P3783', 'P3787', 'P3785', 'P3786', 'P3788', 'P3784')
#
# table_names = [
#     'Liczba lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
#     'Mediana cen za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
#     'Powierzchnia użytkowa lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
#     #'Średnia cena lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (P3786)',
#     'Średnia cena za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
#     'Wartość lokali mieszkalnych sprzedanych w ramach transakcji rynkowych'
# ]
# #
# # code = ''
# #
# # for i, df in enumerate(df_list):
# #     # df.iloc[:, 1].add_prefix(table_names[i])
# #     file = df.to_csv(encoding='UTF-8')
# #
# #     blob = BlobClient.from_connection_string(
# #         code,
# #         container_name='con-gus',
# #         blob_name=table_names[i] + '.csv'
# #     )
# #
# #     blob.upload_blob(file)
#
# storage_account_name = 'pracalicencjacka'
# container_name = 'con-gus'
# storage_key = '9QH+KN4FHq4/cxy6pCQNXoQmvg1SXaj+P8ln3iAj6HBcvB8o3VR0JQMq+Vf6Xb7Ewu+FL9XBcTGQj4tR2TD3tA=='
#
# storage_account_link = get_container_link(storage_account_name, container_name)
#
# df = pd.read_csv(storage_account_link + 'Liczba lokali mieszkalnych sprzedanych w ramach transakcji rynkowych.csv')
# print(df)
