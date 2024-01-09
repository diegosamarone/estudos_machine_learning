![Spyder](https://img.shields.io/badge/Spyder-838485?style=for-the-badge&logo=spyder%20ide&logoColor=maroon)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
<img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="90" height="45">

<html>

  <h1>Regressão Linear</h1>
  <h2>Análise e Predição de Preços de Imóveis nos EUA</h2>


<body>

  <h1>Objetivo do Código:</h1>
  <p>O objetivo deste código é realizar uma análise exploratória dos dados contidos no conjunto 'USA_Housing.csv', que representa informações sobre imóveis nos Estados Unidos. Em seguida, o código constrói um modelo de regressão linear para prever os preços dos imóveis com base em diversas variáveis independentes.</p>

  <h1>Bibliotecas Utilizadas:</h1>
  <ul>
    <li>scikit-learn : Para utilizaçao dos métodos e modelos de aprendizagem de máquina.</li>
    <li>pandas (pd): Utilizada para manipulação e análise de dados.</li>
    <li>numpy (np): Utilizada para suporte a operações matemáticas.</li>
    <li>seaborn (sns): Biblioteca de visualização de dados baseada no Matplotlib.</li>
    <li>matplotlib.pyplot (plt): Utilizada para a criação de gráficos.</li>
  </ul>

  <h1>Passos Realizados:</h1>

  <h2>1. Leitura do Arquivo e Exploração dos Dados:</h2>
  <p>O código inicia lendo o arquivo 'USA_Housing.csv' usando o Pandas e exibe as primeiras linhas e as colunas do conjunto de dados para uma rápida exploração.</p>

  <h2>2. Análise de Linearidades entre os Dados:</h2>
  <p>O código utiliza a função pairplot do Seaborn para criar um gráfico de dispersão entre pares de variáveis, o que possibilita visualizar as relações lineares entre elas.</p>

  <h2>3. Seleção de Variáveis Preditoras (X) e Resposta (y):</h2>
  <p>As variáveis preditoras foram escolhidas para formar a matriz X de treino, enquanto a variável de teste(y) foi definida como os preços dos imóveis.</p>

  <h2>4. Divisão dos Dados em Treino e Teste:</h2>
  <p>Os dados foram divididos em conjuntos de treino e teste utilizando o método train_test_split do scikit-learn.</p>
  
  <h2>5. Construção do Modelo de Regressão Linear:</h2>
  <p>Um modelo de regressão linear foi criado utilizando a classe LinearRegression do scikit-learn. O ajuste do modelo foi realizado com
    os dados de treino.</p>

  <h2>6. Avaliação do Modelo:</h2>
  <p>Foram geradas previsões utilizando os dados de teste e, em seguida, avaliadas as métricas de desempenho do modelo.</p>

  <p>Métricas de Avaliação:
   <li>Erro Absoluto Médio (MAE): Média das diferenças absolutas entre as previsões e os valores reais.</li>
   <li>Média do Quadrado do Erro (MSE): Média das diferenças ao quadrado entre as previsões e os valores reais.</li>
   <li>Raiz do Erro Médio Quadrado (RMSE): Raiz quadrada do MSE, representando uma métrica de erro em escala semelhante à variável de
     resposta.</li>
  
  <!-- Adicionar os demais passos seguindo a estrutura do HTML -->

  <h1>Conclusão:</h1>
  <p>O código forneceu uma análise exploratória dos dados, construção de um modelo de regressão linear e a visualização dos coeficientes do modelo. Foi possível prever os preços de imóveis nos EUA com métricas e visualizações oferecendo insights valiosos sobre o desempenho. Este projeto serve como um exemplo básico de construção e avaliação de modelos de machine learning para problemas de regressão.</p>

</body>

</html>
