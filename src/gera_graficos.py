import sqlite3
import matplotlib.pyplot as plt

def graficos(cursor, atributo):
    #Consulta os dados de curso da tabela
    consulta_sql = "SELECT {0}, COUNT(*) FROM respostas GROUP BY {0}".format(atributo)
    cursor.execute(consulta_sql)
    dados_atributo = cursor.fetchall()

    # Extrai os dados do atributo e as contagens
    valores_atributo = [dados[0] for dados in dados_atributo]
    contagens = [dados[1] for dados in dados_atributo]

    # Gera o gráfico de pizza
    plt.figure(figsize=(10, 8))
    plt.pie(contagens, labels=valores_atributo, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de {} dos Alunos'.format(atributo.capitalize()))
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

#Cria o menu de opções para o usuário
def menu():
    return """
==================================
Escolha qual gráfico deseja gerar:
==================================
1. Gráfico de altura dos alunos
2. Gráfico de idade dos alunos
3. Gráfico de Cursos
4. Gráfico de Satisfação dos alunos
"""

#Recebe a opção escolhida pelo usuário e retorna ela
def opcao():
    option = 0
    user_input = input(menu())  #Recebe a opção do usuário

    switcher = {
        1: "Altura",
        2: "Idade",
        3: "Cursos",
        4: "Satisfacao_g",
    }

    if user_input.isdigit():    #Teste para saber se o usuário digitou um número
        option = switcher.get(int(user_input))
    if option:  #Teste para saber se o número digitado é válido
        return option
    else:
        print("Opção inválida")
        return opcao()  #Chama recursivamente novamente o método caso o número seja inválido

#Testa qual o gráfico que queremos criar e chama passando o atributo certo
def chama_grafico(cursor):
    grafico = opcao()
    if grafico == "Altura":
        graficos(cursor, "altura")
    elif grafico == "Idade":
        graficos(cursor, "idade")
    elif grafico == "Cursos":
        graficos(cursor, "curso")
    elif grafico == "Satisfacao_g":
        graficos(cursor,"satisfacao")

#Função Main()
def main(): 
    conn = sqlite3.connect("database\\dados.db")  #Conecta ao banco de dados
    cursor = conn.cursor()
    chama_grafico(cursor)  #Chama função responsável por ver qual gráfico deve ser criado
    conn.close()  #Fecha a conexão com o banco de dados

if __name__ == "__main__":
  main()