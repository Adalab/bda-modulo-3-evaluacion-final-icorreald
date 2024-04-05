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

# drop datos que no aportan valor
df = sl.drops(df)
df['salary'] = df['salary'].apply(lambda x: abs(x))
#%%
display(df.head())
print(df.shape)
# %%
df.to_csv('fligh-data-clean.csv')
# %%
