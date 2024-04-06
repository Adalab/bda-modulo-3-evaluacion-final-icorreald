#%%
from src import soporte_limpieza as sl
import pandas as pd
import numpy as np

# LIMPIEZA DE CV

activity = pd.read_csv("csv-archivos/Customer Flight Activity.csv", index_col=0)
loyalty = pd.read_csv("csv-archivos/Customer Loyalty History.csv", index_col=0)


# sondeo general de los datos de nuestros df
sl.exploracion_basica([activity,loyalty])


# las unimos para crear un únifo df
df = sl.nuevo_df(activity, loyalty, 'left', 'Loyalty Number')

# homogeneizamos df
sl.homog_tablas([df])

# drop datos que no aportan valor
df = sl.drops(df)
df['salary'] = df['salary'].apply(lambda x: abs(x))

display(df.head())
print(df.shape)

df.to_csv('csv-archivos/flight-data-clean.csv')


#%%
# EVALUACIÓN: DIFERENCIAS EN RESERVAS DE VUELOS POR NIVEL EDUCATIVO
from src import analisis_soporte as ans

# preparación de los DF que vamos a usar
df_testA = ans.prep_df(df, 'A')
df_testB = ans.prep_df(df, 'B')

# display de estadísitcas
display(df_testA.groupby('education')['flights booked'].agg(['mean','mean','std','var']))
display(df_testB.groupby('education')['flights booked'].agg(['mean','mean','std','var']))

# %%
# A/B testing

    ## TEST SAPHIRO
ans.normalidad(df_testA, 'flights booked')
ans.normalidad(df_testB, 'flights booked')

    ## MANN WHITNEY (1)
ans.test_man_whitney(df_testA, ['flights booked'], 'A', 'B', 'grupo')
ans.test_man_whitney(df_testB, ['flights booked'], 'A', 'B', 'grupo')

    ## MANN WHITNEY (2)
ans.test_man_whitney(df_testA, ['flights booked'], 'C', 'D', 'grupo2')
ans.test_man_whitney(df_testB, ['flights booked'], 'C', 'D', 'grupo2')

# %%
# KRUSKAL-WALLIS
ans.kruskal_wallis(df_testA[df_testA['education']=='bachelor']['flights booked'], df_testA[df_testA['education']=='college']['flights booked'], df_testA[df_testA['education']=='master']['flights booked'], df_testA[df_testA['education']=='doctor']['flights booked'],df_testA[df_testA['education']=='high school or below']['flights booked'])
ans.kruskal_wallis(df_testB[df_testB['education']=='bachelor']['flights booked'], df_testB[df_testB['education']=='college']['flights booked'], df_testB[df_testB['education']=='master']['flights booked'], df_testB[df_testB['education']=='doctor']['flights booked'],df_testB[df_testB['education']=='high school or below']['flights booked'])