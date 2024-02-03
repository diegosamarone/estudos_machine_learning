![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
<img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="90" height="45">

<html>
  
<body>
<h1>Projeto K Nearest Neighbors (KNN) com Python</h1>
<br>
  <h2>Introdução</h2>
  <p>O algoritmo K-Nearest Neighbors (KNN) é um método de aprendizado supervisionado não paramétrico que pode ser usado para classificação e regressão. Ele se baseia na ideia de que pontos de dados semelhantes estão próximos no espaço de características, com a proximidade geralmente medida pela distância euclidiana.</p>
  <p>No KNN, um novo ponto de dados é classificado ou previsto com base nos ‘K’ pontos de dados mais próximos do conjunto de treinamento. Para classificação, o novo ponto é atribuído à classe mais comum entre seus ‘K’ vizinhos. Para regressão, o valor previsto é a média dos valores dos ‘K’ vizinhos.</p>
  <p>A escolha do valor de ‘K’ é crucial para a precisão do modelo. Um ‘K’ muito pequeno pode tornar o modelo excessivamente sensível ao ruído, resultando em sobreajuste. Por outro lado, um ‘K’ muito grande pode tornar o modelo insensível às diferenças entre as classes, levando a um subajuste. Portanto, a seleção adequada de ‘K’ é essencial para o desempenho do KNN.</p>
  <p>Para fins de estudos, utilizamos um conjunto de dados classificados de uma empresa, ocultando os parâmetros específicos. O objetivo foi aplicar o KNN para prever a classe de um novo ponto de dados com base nos parâmetros.</p>
  <h4>Pré-processamento de Dados</h4>
  <p>Após obter e carregar os dados, realizamos a normalização das variáveis. Isso é crucial para o KNN, já que a distância entre pontos determina os vizinhos mais próximos. A normalização garante que todas as variáveis contribuam igualmente, independentemente da escala original.</p>
  <h4>Divisão dos Dados</h4>
  <p>Os dados foram divididos em conjuntos de treino e teste, seguindo as melhores práticas de avaliação de modelos.</p>
  <h4>Implementação do KNN</h4>
  <p>Utilizamos a biblioteca scikit-learn para implementar o KNN. Iniciamos com k=1 e posteriormente escolhemos o valor de k ideal usando o método do cotovelo, que avalia diferentes valores de k em termos de taxa de erro.</p>
  <h4>Avaliação do Modelo</h4>
  <p>Avaliamos o modelo usando métricas como matriz de confusão, precisão, recall e F1-score. A escolha de k=23 resultou em um desempenho notável, com alta precisão e recall para ambas as classes.</p>
  <h4>Conclusão</h4>
  <p>Em resumo, o modelo KNN com k=23 apresentou um desempenho satisfatório na classificação das classes, com uma acurácia geral de 93%. O projeto destaca a importância da escolha adequada de k para o bom desempenho do KNN.</p>
  
</body>

</html>

