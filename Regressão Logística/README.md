![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
<img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="90" height="45">

<html>
<body>

  <h1>Regressão Logística</h1>
  
  <p>A regressão logística é um método de classificação usado para prever a probabilidade de ocorrência de um evento com base em variáveis independentes. A variável dependente é limitada entre 0 e 1, representando a probabilidade do evento ocorrer.</p>
  
  <h3>Exemplos de Problemas de Classificação:</h3>
  <ul>
    <li>Filtro de e-mails </li>
    <li>Modelos preditores de clientes inadimplentes</li>
    <li>Diagnóstico de doenças</li>
  </ul>
  
  <p>A regressão logística é útil para prever categorias discretas, estimando a probabilidade de uma observação pertencer a uma classe específica. A função logística (sigmoid) mapeia qualquer número real para um valor entre 0 e 1.</p>

  <p>Após treinarmos um modelo de regressão logística, é comum testá-lo em um conjunto de dados de teste. A matriz de confusão é uma ferramenta essencial para avaliar o desempenho do modelo. Ela consiste uma tabela que compara as previsões do modelo com os valores reais. Ela é composta por quatro componentes principais:</p>
    <ul>
    <li>Verdadeiro Positivo (VP): O modelo previu corretamente a classe positiva.</li>
    <li>Verdadeiro Negativo (VN): O modelo previu corretamente a classe negativa.</li>
    <li>Falso Positivo (FP): O modelo previu incorretamente a classe positiva. Também conhecido como Erro Tipo I.</li>
    <li>Falso Negativo (FN): O modelo previu incorretamente a classe negativa. Também conhecido como Erro Tipo II.</li>
  </ul>
  <h2> </h2>
<h3>Segue abaixo as informações sobre o estudo realizado para este modelo de machine learnig</h3>
  <h2>Análise e Predição dos dados sobre o Titanic</h2>
  
  <p>Nesta análise, exploramos o Conjunto de dados do Titanic da Kaggle, conhecido por ser um ponto de partida comum em Machine Learning. Utilizamos a regressão logística em Python para desenvolver um algoritmo de classificação, distinguindo entre passageiros sobreviventes e falecidos.</p>

[Link para o Notebook Jupyter](https://github.com/diegosamarone/estudos_machine_learning/blob/main/Regress%C3%A3o%20Log%C3%ADstica/Regress%C3%A3o%20log%C3%ADstica%20com%20Python.ipynb)
  
  <h3>Importar bibliotecas</h3>
  <p>Iniciamos importando as bibliotecas necessárias para nossa análise, incluindo pandas, numpy, seaborn, matplotlib e ferramentas de machine learning.</p>

  <h3>Análise de dados exploratórios</h3>
  <p>Ao ler o arquivo titanic_train.csv em um DataFrame pandas, começamos a análise exploratória dos dados. Utilizamos seaborn para criar um mapa de calor, identificando áreas com dados ausentes, e observamos que aproximadamente 20% dos dados de idade estão faltando.</p>

  <h3>Visualizações Gráficas</h3>
  <p>Definimos gráficos para explorar a distribuição de sobreviventes por classe de passageiros, gênero, idade, acompanhantes no navio e preços de tickets. Esses gráficos fornecem insights sobre padrões e tendências nos dados.</p>

 

  <h3>Limpeza de Dados</h3>
  <p>Para lidar com dados de idade faltantes, implementamos uma estratégia inteligente de imputação, considerando a idade média por classe de passageiros. Além disso, removemos a coluna 'Cabin' e uma linha com dados ausentes em 'Embarked'.</p>

  <h3>Conversão de Categóricos</h3>
  <p>Para preparar os dados para o modelo, convertemos características categóricas em variáveis dummy usando pandas, garantindo que o algoritmo de Machine Learning possa processar esses dados corretamente.</p>

  <h3>Construção do Modelo de Regressão Logística</h3>
  <p>Dividimos os dados em conjuntos de treinamento e teste, construindo um modelo de regressão logística para prever a sobrevivência dos passageiros.</p>

  <h3>Avaliação do Modelo</h3>
  <p>Avaliamos o desempenho do modelo usando métricas como precisão, recall e pontuação F1 por meio do relatório de classificação. A matriz de confusão (148 Verdadeiros Negativos, 15 Falsos Positivos, 39 Falsos Negativos e 65 Verdadeiros Positivos) forneceu uma visão detalhada do desempenho do modelo.</p>



</body>
</html>
