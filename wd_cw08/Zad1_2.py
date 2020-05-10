import pandas as pd
import numpy as np


df = pd.read_excel('imiona.xlsx')
#liczba imion wieksza od 1000 w roku 2000
print(df[(df.Liczba > 1000) & (df.Rok==2000)])
#nadane imie takie samo
print(df[df.Imie=="ADAM"])
#suma urodzonych dzieci
print(df.agg({'Liczba':['sum']}))
#suma urodzonych dzieci w latach 2000-2005
print(df.loc[df['Rok'] < 2006, 'Liczba'].sum())
#suma urodzonych chłopców i dziewczynek
print(df.groupby(['Plec']).agg({'Liczba':['sum']}))
