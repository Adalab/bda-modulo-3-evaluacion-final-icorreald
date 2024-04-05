import pandas as pd
import numpy as np

#%%
# datos básicos sobre df
def exploracion_basica(lista_df):
    for df in lista_df:
       display(df.head())
       print(df.shape)
       print('')
       print(df.isnull().sum()/df.shape[0]*100)
       print('')
       print(df.dtypes)
       for columna in df.select_dtypes(include='O'):
        print(df[columna].value_counts())
        print('')

       print('-'*20) 

# renombrar columnas
def nuevas_columnas(df):
    nuevas_columnas = {columna: columna.lower() for columna in df.columns}
    return df.rename(columns=nuevas_columnas, inplace= True)

# string to lower
def unify(valor):
    try:
        return valor.lower().strip()
    except:
        return valor

# aplicar cambios a df    
def homog_tablas(lista_df):
    for df in lista_df:
        nuevas_columnas(df)
    
    for df in lista_df:
        for columna in df.columns:
            df[columna] = df[columna].apply(unify)

# drop datos que no aportan valor
def drops(df):
    df.drop_duplicates(inplace=True)
    df.drop(columns=['cancellation month', 'cancellation year'], axis=1, inplace=True)
    df = df.drop(df[(df['education']=='high school or below') & (df['salary'] < 0)].index)
    return df