from IPython.display import IFrame
IFrame('http://pandas.pydata.org/', width=1000, height=350)

import pandas as pd
import numpy as np

# Cómo cargar y guardar datos desde diferentes fuentes
df_txt = pd.read_csv("data/medidas.txt", header=None, parse_dates=[1], keep_date_col=True)
#df_txt = pd.read_csv('data/all_test.txt', sep='\t', header=None)
df_txt

df_other_excel = pd.read_excel('data/other_demo.xls', 'Brasil (bio+socio)') # ver que sucede cuando ponemos header None
print df_other_excel.columns
df_other_excel

df_excel = pd.read_excel('data/demo.xls', 'Sheet1', header=None)
df_excel

df_html = pd.read_html('data/lista_landmark.html')
df_html

#df_txt.to_excel('data/test_out.xls', header=False, index=False) # cuidado con límites de planillas de excel!

df_excel.to_csv('data/test_out.txt', index=False)
df_excel.to_clipboard

# estructuras de Pandas
# Series
import pandas as pd
mi_serie = pd.Series([3.4, 56.3, 56.1])
print (mi_serie.values)
print (mi_serie.index)
mi_serie

mi_serie = pd.Series([3.4, 56.3, 56.1], index=['dist_1', 'dist_2', 'dist_3'])
print (mi_serie.values)
print (mi_serie.index)
print (mi_serie['dist_2'])
print (mi_serie[['dist_1', 'dist_3']])
mi_serie

mi_serie[mi_serie > 4]

pd.notnull(mi_serie)

pd.isnull(mi_serie)

# Series Temporales
dates_complete = pd.date_range('1/18/2013', '02/09/2014', freq='15T')
other_dates = pd.date_range('1/18/2013', '02/09/2014', freq='1D')
print (dates_complete)
print (other_dates)
mi_serie = pd.Series(other_dates)
mi_serie_med = pd.Series(dates_complete)

# DataFrames
type(df_excel)

df_other_excel

df_other_excel[['6.8 VIDEO', 'EYE COLOR']]

print df_txt.columns
df_txt.columns = ['medidor', 'date', 'value']
print df_txt.columns
df_txt
df_txt['medidor'].drop_duplicates()
