<h1>Programa de Análise de Dados de Alunos</h1>
<h3>Este é um programa Python que permite analisar os dados dos alunos, coletados a partir de um formulário do Google, armazenados em um banco de dados SQLite.</h3>
<br>
<h4>Funcionalidades</h4>
<p>1 - Leitura de Dados: O programa lê dados de uma planilha do Google Sheets usando a API gspread.</p>
<p>2 - Armazenamento de Dados: Os dados lidos são armazenados em um banco de dados SQLite local.</p>
<p>3 - Análise de Dados: O programa permite analisar os dados armazenados no banco de dados, incluindo distribuição de altura, idade, curso e satisfação dos alunos.</p>
<p>4 - Visualização de Dados: Os dados podem ser visualizados através de gráficos gerados com a biblioteca matplotlib.</p>
<br>
<h4>Configuração</h4>
<p>Instale as dependências do programa que estão no diretório "info", dentro do arquivo <code>requirements.txt</code>. Você pode fazer isso executando o seguinte comando no terminal:</p>
<pre>pip install -r requirements.txt</pre>
<p>Isso instalará todas as bibliotecas Python necessárias, como "gspread" e "matplotlib".</p>
<br>
<h4>Após ter instalado todas as dependências siga as instruções abaixo:</h4>
<p>1 - Certifique-se de ter uma conta de serviço do Google criada e o arquivo JSON de credenciais baixado. Link para o passo a passo: <a href="https://docs.gspread.org/en/latest/oauth2.html">Instruções de Configuração da Conta do Google</a></p>
<p>2 - Mude o nome do arquivo na linha 8 do script <code>coleta_dados.py</code> para o nome da sua planilha.</p>
<p>3 - Execute o script Python <code>coleta_dados.py</code> para coletar os dados dos alunos da planilha do Google e armazená-los no banco de dados SQLite.</p>
<p>4 - Execute o script Python <code>gera_graficos.py</code> para visualizar os dados em gráficos usando a biblioteca matplotlib.</p>
<br>
<h4>Formulário</h4>
<p>Link para o formulário de teste: <a href="https://docs.google.com/forms/d/e/1FAIpQLSeOjvzpRUKEItgwS2i1BmJlJ4h9k0wtl8Bws-PRrYwt6aqoSA/viewform?usp=sf_link">Avaliação de Ensino</a></p>
<p>Link do Google Sheets com os resultados dos formulários:  <a href="https://docs.google.com/spreadsheets/d/1Altyu6NEUdBXaYQ-eLkNohQWsARg00lMAn8yc-8dVRc/edit?usp=sharing">Avaliação de ensino (Respostas)</a></p>
<br>
<h4>Licença</h4>
<p>Este projeto é licenciado sob a Licença MIT - veja o arquivo <code>LICENSE</code> para detalhes.</p>
