![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
<img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="90" height="45">

<html>
  
<body>
<h1>Random Forest com Python</h1>
<br>
<h3>Introdução</h3>
<p>Florestas Aleatórias é um método de aprendizado de máquina que combina <b>várias árvores de decisão</b> para produzir um resultado mais preciso. Cada árvore na floresta é um modelo independente que usa um subconjunto aleatório de características para fazer previsões.</p>
<div align="center">
<img style="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-out;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://bookdown.org/jessicakubrusly/intr-machine-learning-i/_book/imagens/RF.png" width="500" height="400">
</div>
<p>Por exemplo, em um sistema de recomendação de filmes, as variáveis como gênero do filme, duração, diretor e atores principais podem ser usadas para prever se um usuário gostará de um filme que ainda não assistiu. Isso é feito através de árvores de decisão, onde cada nó divide a árvore com base no valor de um atributo, e a escolha do atributo é feita com base em conceitos como Entropia e Ganho de Informação.</p>
  <b>Nas árvores de decisão temos:</b>
  <ul>
    <li>Nós: Divide a árvore por um valor de um certo atributo.</li>
    <li>Ramos: Saída de um nó.</li>
    <li>Raíz: Nó que faz a primeira divisão</li>
    <li>Folha: Nó final, que toma a decisão.</li>
    <div align="center">
    <img style="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://colaborae.com.br/wp-content/uploads/2023/07/arvore.png" width="500" height="300">
    </div>
  </ul>
  
<p>No entanto, as árvores de decisão podem sofrer de <b>overfitting</b>, pois elas aprendem muito bem as características do conjunto de dados de treinamento, mas podem não generalizar bem para novos dados. Para mitigar isso, o método de <b>Florestas Aleatórias</b> é usado, que cria "múltiplas árvores" de decisão usando diferentes divisões do conjunto de dados e parâmetros aleatórios para cada divisão. Isso ajuda a melhorar a precisão e a confiabilidade das previsões.</p>
  
<h4>Vantagens das Florestas Aleatórias em relação a uma única árvore de decisão:</h4>
    <ul>
        <li>Elas são mais precisas, especialmente quando o conjunto de dados é grande e complexo.</li>
        <li>São resistentes ao overfitting.</li>
        <li>Lidam melhor com outliers e absorvem melhor a informação contida em cada covariável.</li>
    </ul>

<h3>Exemplo prático com Python</h3>
<p>Para abordar o modelo <b>Random Forest</b> com python, começaremos trabalhando com dados sobres pacientes com problema de corcunda e tentaremos predizer se apenas uma cirurgia corretora será ou não suficiente.</p>

<h4>Referências:</h4>
    <ul>
        <li><a href="https://www.ibm.com/br-pt/topics/random-forest" target="_blank">O que é Floresta Aleatória? | IBM</a></li>
        <li><a href="https://datascience.eu/pt/programacao/entendendo-os-classificadores-de-florestas-aleatorias-em-python/" target="_blank">Florestas Aleatórias — Programação — DATA SCIENCE</a></li>
        <li><a href="https://bookdown.org/jessicakubrusly/intr-machine-learning-i/_book/cap-floresta.html" target="_blank">Capítulo 4 Floresta Aleatória | Introdução ao Machine Learning - I</a></li>
        <li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html" target="_blank">sklearn.ensemble.RandomForestClassifier - scikit-learn</a></li>
        <li><a href="https://bing.com/search?q=Florestas+Aleat%c3%b3rias+machine+learning" target="_blank">O que é Floresta Aleatória? | IBM</a></li>
        <li><a href="https://didatica.tech/o-que-e-e-como-funciona-o-algoritmo-randomforest/" target="_blank">Entenda como funciona o Random Forest (Machine Learning)</a></li>
        <li><a href="https://bing.com/search?q=documenta%c3%a7%c3%a3o+python+Florestas+Aleat%c3%b3rias" target="_blank">Um guia prático para implementar um classificador Random Forest em Python</a></li>
        <li><a href="https://acervolima.com/regressao-aleatoria-da-floresta-em-python/" target="_blank">Regressão aleatória da floresta em Python – Acervo Lima</a></li>
        <li><a href="https://ichi.pro/pt/um-guia-pratico-para-implementar-um-classificador-random-forest-em-python-166685681689187" target="_blank">Um guia prático para implementar um classificador Random Forest em Python</a></li>
    </ul>
  
</body>

</html>

