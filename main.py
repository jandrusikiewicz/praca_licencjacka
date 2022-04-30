from scripts import *

code = 'DefaultEndpointsProtocol=https;AccountName=pracalicencjacka;AccountKey=9QH+KN4FHq4/cxy6pCQNXoQmvg1SXaj' \
       '+P8ln3iAj6HBcvB8o3VR0JQMq+Vf6Xb7Ewu+FL9XBcTGQj4tR2TD3tA==;EndpointSuffix=core.windows.net'

with open('tabela_kwartalne') as f:
    tabela_kwartalne = f.read()

with open('tabela_roczne') as f:
    tabela_roczne = f.read()

tabela_kwartalne = json.loads(tabela_kwartalne)
tabela_roczne = json.loads(tabela_roczne)

kody_grup_roczne = [*tabela_kwartalne.keys()]
kody_grup_kwartalne = [*tabela_kwartalne.keys()]

nazwy_grup_roczne = [*tabela_kwartalne.values()]
nazwy_grup_kwartalne = [*tabela_kwartalne.values()]

lata = [2020]

get_and_blob(kody_grup_roczne, 5, lata, nazwy_grup_roczne, code, 'con-gus-roczne')

get_and_blob(kody_grup_kwartalne, 5, lata, nazwy_grup_kwartalne, code, 'con-gus-kwartalne')
