file_dir = r'C:\Users\whittlj2\data\input.csv'
output_dir = r'C:\Users\whittlj2\data\output.xlsx'
delimiter = '|'
data_type = 'str'

import pandas as pd
import numpy as np
import openpyxl as xl

df_file = pd.read_csv(
    file_dir
    , sep = delimiter
    , dtype=data_type
    , engine = 'python')


#writer = pd.ExcelWriter(output_dir, engine = 'openpyxl')
df_file.to_excel(output_dir, index = False)