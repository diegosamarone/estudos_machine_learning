# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:31:32 2023

@author: Diego
"""

'''
Instruções para o usuário:
Execute o código em ordem, célula por célula.

*sugestão: shift + enter.
'''

#%% imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#%% lendo arquivo
usahousing = pd.read_csv('USA_Housing.csv')

usahousing.head()
usahousing.columns

#%% identificando linearidades entres os dados
sns.pairplot(usahousing)



#%%
sns.heatmap(usahousing.iloc[0:, 0:6].corr())

#%% selecionar a variavel x que vai predizer o modelo

X = usahousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

#%% defenir a variavel/resposta que vai ser predita
y = usahousing['Price']

#%% metodo que é capaz de fazer a divisão(split) dos dados (X e y) em dados de treino e teste
from sklearn.model_selection import train_test_split

# train_test_split() vai quebrar o x em duas partes e o y em duas partes
X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

#%%modelo que vamos utilziar
from sklearn.linear_model import LinearRegression

lm = LinearRegression()

#%%Gerando o modelo de machine learnig com os dados de treino
lm.fit(X_train, y_train)

print(lm.intercept_)

print(lm.coef_)

#%%
coefs = pd.DataFrame(lm.coef_, X.columns, columns=['Coefs'])

#%% predizendo preços de casas
predict = lm.predict(x_test) #aprender os parametros das primeiras casas

#%%
plt.figure(figsize=(12, 6))
plt.scatter(y_test, predict)    
# o eixo x mostra os valores corretos das casas
# e no eixo y, temos os valores que o modelo predizeu

#%% Vamos agora plotar o grafico de distribuição do erros(resíduos)    
sns.displot((y_test - predict))
    
'''   Métricas de avaliação de Regressão

Erro Absoluto Médio (Mean Absolute Error - MAE)
Média do Quadrado do Erro (Mean Squared Error - MSE)
Raiz do Erro Médio Quadrado (Root Mean Squared - Error - RMSE)

'''
#%%
from regressao_linear_estudos import y_test, predict, np
from sklearn import metrics

#%%  Erro Absoluto Médio (Mean Absolute Error - MAE)
print('MAE:', metrics.mean_absolute_error(y_test, predict))


#%% Média do Quadrado do Erro (Mean Squared Error - MSE)
print('MSE:', metrics.mean_squared_error(y_test, predict))

#%% Raiz do Erro Médio Quadrado (Root Mean Squared - Error - RMSE)
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predict)))

