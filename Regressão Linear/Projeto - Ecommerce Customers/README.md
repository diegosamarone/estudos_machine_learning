![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
<img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="90" height="45">
<html>
<body>
  <h1>Regressão Linear - Projeto</h1>
  <p>Parabéns por embarcar neste projeto de Regressão Linear! Neste desafio, você foi contratado por uma empresa de comércio eletrônico baseada em Nova York, que oferece sessões de consultoria em estilo e vestuário, tanto na loja física quanto online. Sua missão é ajudar a empresa a decidir se deve focar seus esforços no desenvolvimento do aplicativo móvel ou no site.</p>
  <h2>Overview do Projeto</h2>
  <ol>
    <li><strong>Objetivo:</strong> Determinar se a empresa deve concentrar seus esforços no aplicativo móvel ou no site com base em dados do cliente.</li>
    <li><strong>Dados Disponíveis:</strong>
      <ul>
        <li>Avg. Session Length: Tempo médio das sessões de consultoria de estilo na loja.</li>
        <li>Time on App: Tempo médio gasto no aplicativo em minutos.</li>
        <li>Time on Website: Tempo médio gasto no site em minutos.</li>
        <li>Length of Membership: Tempo em anos que o cliente é membro.</li>
      </ul>
    </li>
    <li><strong>Etapas Realizadas:</strong>
      <ul>
        <li>Importação e configuração de bibliotecas.</li>
        <li>Leitura e análise inicial dos dados.</li>
        <li>Exploração visual usando seaborn para identificar relações entre variáveis.</li>
        <li>Treinamento de um modelo de Regressão Linear.</li>
        <li>Avaliação do modelo usando dados de teste.</li>
      </ul>
    </li>
  </ol>
  <h2>Resultados e Conclusões</h2>
  <ul>
    <li><strong>Correlações Identificadas:</strong>
      <ul>
        <li>O tempo gasto no aplicativo tem uma correlação mais forte com o volume anual gasto em comparação com o tempo no site.</li>
        <li>A duração da associação tem o maior impacto no volume anual gasto.</li>
      </ul>
    </li>
    <li><strong>Coeficientes do Modelo:</strong>
      <ul>
        <li>Avg. Session Length: Aumento de 25 dólares no gasto médio anual por unidade de tempo.</li>
        <li>Time on App: Cada minuto adicional gasto no aplicativo corresponde a um aumento de 38 dólares no gasto médio anual.</li>
        <li>Length of Membership: Aumento de 61 dólares no gasto médio anual por ano de associação.</li>
      </ul>
    </li>
    <li><strong>Recomendação para a Empresa:</strong>
      <ul>
        <li>Com base nos coeficientes, sugere-se que a empresa deve concentrar esforços no desenvolvimento do aplicativo móvel.</li>
        <li>A duração da associação do cliente é crucial, desta forma deve-se criar estratégias para retenção e fidelização dos clientes.</li>
      </ul>
    </li>
    <li><strong>Avaliação do Modelo:</strong>
      <ul>
        <li>Erro Absoluto Médio (MAE): 7.23</li>
        <li>Erro Quadrado Médio (MSE): 79.81</li>
        <li>Raiz Quadrada do Erro Quadrado Médio (RMSE): 8.93</li>
      </ul>
    </li>
  </ul>
  <p>Este projeto oferece insights valiosos para a tomada de decisões estratégicas da empresa, fornecendo uma base sólida para futuras ações e investimentos.</p>
  <h1>Bibliotecas Utilizadas:</h1>
  <ul>
    <li>scikit-learn : Para utilizaçao dos métodos e modelos de aprendizagem de máquina.</li>
    <li>pandas (pd): Utilizada para manipulação e análise de dados.</li>
    <li>numpy (np): Utilizada para suporte a operações matemáticas.</li>
    <li>seaborn (sns): Biblioteca de visualização de dados baseada no Matplotlib.</li>
    <li>matplotlib.pyplot (plt): Utilizada para a criação de gráficos.</li>
  </ul>
</body>
</html>
