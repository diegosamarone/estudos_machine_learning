![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
<img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="90" height="45">

<html>
<body>
<h1>Projeto de Regressão Logística</h1>

<p>Neste projeto, trabalharemos com um conjunto de dados fictício de publicidade para prever se um usuário clicará em um anúncio com base em suas características.</p>
<br>

<h2>Relatório:</h2>
<p>No Notebook deste projeto você vai poder acompanhar as seguintes etapas:</p>

<h3>Conjunto de Dados</h3>
<p>O conjunto de dados inclui informações como tempo gasto no site, idade do consumidor, renda média, uso diário da internet e se o usuário clicou ou não no anúncio.</p>

<h3>Importação de Bibliotecas</h3>
<p>Foram importadas as bibliotecas necessárias, incluindo pandas, numpy, matplotlib e seaborn.</p>

<h3>Carregamento dos Dados</h3>
<p>Os dados foram carregados a partir do arquivo 'advertising.csv' em um DataFrame chamado 'ad_data'.</p>

<h3>Visão Geral dos Dados</h3>
<p>Foram exibidas informações sobre o DataFrame, incluindo tipos de dados e quantidade de entradas em cada coluna.</p>

<h3>Resumo Estatístico</h3>
<p>Foi gerado um resumo estatístico para as colunas numéricas do DataFrame.</p>

<h3>Análise Exploratória de Dados</h3>
<p>Foram criados gráficos usando a biblioteca Seaborn para explorar as relações entre variáveis, incluindo histograma de idade, jointplot de renda e idade, distribuições KDE de tempo gasto no site vs idade, e jointplot de tempo gasto no site vs uso diário da internet.</p>

<h3>Regressão Logística</h3>
<p>Os dados foram divididos em conjuntos de treino e teste, e um modelo de Regressão Logística foi treinado usando as colunas selecionadas. A precisão do modelo foi calculada e uma matriz de confusão foi apresentada.</p>

<h3>Resultados e Conclusões</h3>
<p>O modelo de Regressão Logística apresentou uma precisão de aproximadamente 90.61%. A matriz de confusão revelou valores para verdadeiros positivos, verdadeiros negativos, falsos positivos e falsos negativos. Com base nesses resultados, concluímos que o modelo tem um desempenho sólido na previsão de cliques em anúncios com base nas características fornecidas no conjunto de dados.</p>


</body>
</html>
