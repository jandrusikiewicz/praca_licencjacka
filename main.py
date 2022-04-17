from azure.storage.blob import BlobClient

from scripts import *

pd.set_option('display.max_columns', None)

# print(get_variables('P3783').to_string())
# print(get_data_by_variable('633617').head(1000))
df_list = get_multiple_subjects('P3783', 'P3787', 'P3785', 'P3786', 'P3788', 'P3784')

table_names = [
    'Liczba lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
    'Mediana cen za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
    'Powierzchnia użytkowa lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
    'Średnia cena lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (P3786)',
    'Średnia cena za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
    'Wartość lokali mieszkalnych sprzedanych w ramach transakcji rynkowych'
]

code = ''

for i, df in enumerate(df_list):
    # df.iloc[:, 1].add_prefix(table_names[i])
    file = df.to_csv(encoding='UTF-8')

    blob = BlobClient.from_connection_string(
        code,
        container_name='con-gus',
        blob_name=table_names[i] + '.csv'
    )

    blob.upload_blob(file)
