import json

from scripts import *

pd.set_option('display.max_columns', None)

code = 'DefaultEndpointsProtocol=https;AccountName=pracalicencjacka;AccountKey=9QH+KN4FHq4/cxy6pCQNXoQmvg1SXaj' \
       '+P8ln3iAj6HBcvB8o3VR0JQMq+Vf6Xb7Ewu+FL9XBcTGQj4tR2TD3tA==;EndpointSuffix=core.windows.net '

# tables_names_roczne = [
#        'Liczba lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
#        'Mediana cen za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
#        'Powierzchnia użytkowa lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
#        'Średnia cena lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (P3786)',
#        'Średnia cena za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych',
#        'Wartość lokali mieszkalnych sprzedanych w ramach transakcji rynkowych'
# ]
# subject_list_roczne = ['P3783', 'P3787', 'P3785', 'P3786', 'P3788', 'P3784']
#
# tables_names_kwartalne = [
#        'Liczba lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
#        'Mediana cen za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
#        'Powierzchnia użytkowa lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
#        'Średnia cena lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (P3786) (dane kwartalne)',
#        'Średnia cena za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)',
#        'Wartość lokali mieszkalnych sprzedanych w ramach transakcji rynkowych (dane kwartalne)'
# ]
# subjects_list_kwartalne = ['P3789', 'P3793', 'P3791', 'P3792', 'P3794', 'P3790']

# reading the data from the file
with open('tabela_kwartalne.json') as f:
    tabela_kwartalne = f.read()

with open('tabela_roczne.json') as f:
    tabela_roczne = f.read()

tabela_kwartalne = json.loads(tabela_kwartalne)
tabela_roczne = json.loads(tabela_roczne)

years = [2018, 2019, 2020]

kody_grup_roczne = tabela_kwartalne.keys()
kody_grup_kwartalne = tabela_kwartalne.keys()

nazwy_grup_roczne = tabela_kwartalne.values()
nazwy_grup_kwartalne = tabela_kwartalne.values()

get_and_blob(kody_grup_roczne, 5, years, nazwy_grup_roczne, code, 'con-gus-roczne')

get_and_blob(kody_grup_kwartalne, 5, years, nazwy_grup_kwartalne, code, 'con-gus-kwartalne')
