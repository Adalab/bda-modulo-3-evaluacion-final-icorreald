#%%
from src import soporte_limpieza as sl
import pandas as pd
import numpy as np

#%%
activity = pd.read_csv("Customer Flight Activity.csv", index_col=0)
loyalty = pd.read_csv("Customer Loyalty History.csv", index_col=0)

#%%
# sondeo general de los datos de nuestros df
sl.exploracion_basica([activity,loyalty])

# homogeneizamos nuestras tablas
sl.homog_tablas([activity, loyalty])

# las unimos para crear un únifo df
df = activity.merge(loyalty, how='left', on='Loyalty Number')

# eliminamos las columnas y filas que no nos aportan datos
    # columnas
df.drop(columns=['cancellation month', 'cancellation year'], axis=1, inplace=True)

    # filas
df = df.drop(df[(df['education']=='high school or below') & (df['salary'] < 0)].index)

#%%
display(df.head())






# %%
print(df.shape)
# %%
