from scripts import *

code = 'DefaultEndpointsProtocol=https;AccountName=pracalicencjacka;AccountKey=9QH+KN4FHq4/cxy6pCQNXoQmvg1SXaj' \
       '+P8ln3iAj6HBcvB8o3VR0JQMq+Vf6Xb7Ewu+FL9XBcTGQj4tR2TD3tA==;EndpointSuffix=core.windows.net'

lata = [2020]


def main():
    kody_grup_roczne, nazwy_grup_roczne = get_subject_and_names_lists('tabela_roczne')
    kody_grup_kwartalne, nazwy_grup_kwartalne = get_subject_and_names_lists('tabela_kwartalne')

    get_and_blob(kody_grup_roczne, 5, lata, nazwy_grup_roczne, code, 'con-gus-roczne')
    get_and_blob(kody_grup_kwartalne, 5, lata, nazwy_grup_kwartalne, code, 'con-gus-kwartalne')


main()
