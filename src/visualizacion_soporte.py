import matplotlib.pyplot as plt
import seaborn as sns

def barplot(x_valor, y_valor, data_valor, title, color_bars=None, pal_bars=None):
    '''
    x_valor (str) = variable eje x
    y_valor (str) = variable eje y
    data_valor = dataframe de donde extraemos los datos
    title (str) = título de nuestro df
    
    '''
    sns.barplot(x= x_valor,
                y= y_valor,
                data= data_valor,
                color = color_bars,
                palette= pal_bars)
    plt.title(title)
    
    

              