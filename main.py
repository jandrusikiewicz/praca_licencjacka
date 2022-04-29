from scripts import *

pd.set_option('display.max_columns', None)

tables_names_roczne = [
       'Liczba lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
       'Mediana cen za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
       'Powierzchnia użytkowa lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
       'Średnia cena lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (P3786)',
       'Średnia cena za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
       'Wartość lokali mieszkalnych sprzedanych w ramach transakcji rynkowych'
]

tables_names_kwartalne = [
       'Liczba lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
       'Mediana cen za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
       'Powierzchnia użytkowa lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
       'Średnia cena lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (P3786) (dane kwartalne)',
       'Średnia cena za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
       'Wartość lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)'
]

code = 'DefaultEndpointsProtocol=https;AccountName=pracalicencjacka;AccountKey=9QH+KN4FHq4/cxy6pCQNXoQmvg1SXaj' \
       '+P8ln3iAj6HBcvB8o3VR0JQMq+Vf6Xb7Ewu+FL9XBcTGQj4tR2TD3tA==;EndpointSuffix=core.windows.net '

years = [2018, 2019, 2020]

subject_list_roczne = ['P3783', 'P3787', 'P3785', 'P3786', 'P3788', 'P3784']
get_and_blob(subject_list_roczne, 5, years, tables_names_roczne, code, 'con-gus-roczne')

subjects_list_kwartalne = ['P3789', 'P3793', 'P3791', 'P3792', 'P3794', 'P3790']
get_and_blob(subjects_list_kwartalne, 5, years, tables_names_kwartalne, code, 'con-gus-kwartalne')
