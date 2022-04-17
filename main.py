import pandas as pd

from functions import *

pd.set_option('display.max_columns', None)

# print(get_variables('P3783').to_string())
# print(get_data_by_variable('633617').head(1000))
print(get_all_data_from_subject('P3783'))
