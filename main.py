from functions import *

connection_string = "DefaultEndpointsProtocol=https;AccountName=pracalicencjacka;AccountKey=9QH+KN4FHq4/cxy6pCQNXoQmvg1SXaj" \
                    "+P8ln3iAj6HBcvB8o3VR0JQMq+Vf6Xb7Ewu+FL9XBcTGQj4tR2TD3tA==;EndpointSuffix=core.windows.net"


def main() -> None:
    kody_grup_roczne, nazwy_grup_roczne = get_subject_and_names_lists('tabela_roczne.json')
    kody_grup_kwartalne, nazwy_grup_kwartalne = get_subject_and_names_lists('tabela_kwartalne.json')

    get_and_blob(kody_grup_roczne, 5, [2017, 2018, 2019, 2020], nazwy_grup_roczne, connection_string, 'con-gus-roczne')
    get_and_blob(kody_grup_kwartalne, 5, [2017, 2018, 2019, 2020], nazwy_grup_kwartalne, connection_string, 'con-gus-kwartalne')


if __name__ == "__main__":
  main()
