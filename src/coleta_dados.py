import gspread
import sqlite3

#Autentica a conta de serviço
gc = gspread.service_account()

#Abre a planilha desejada
sh = gc.open("Avaliação de ensino (respostas)")

#Acessa a primeira aba da planilha
worksheet = sh.sheet1

#Obtém todos os registros da planilha como uma lista de dicionários
records = worksheet.get_all_records()

#Conecta ao banco de dados SQLite
conn = sqlite3.connect("database\\dados.db")
cursor = conn.cursor()

#Cria uma tabela no banco de dados
cursor.execute("""CREATE TABLE IF NOT EXISTS respostas 
                  (email TEXT PRIMARY KEY, nome TEXT, idade TEXT, altura TEXT, curso TEXT, satisfacao TEXT)""")

#Verifica se um registro já existe antes de inseri-lo
for record in records:
    cursor.execute("SELECT email FROM respostas WHERE email=?", (record['Email'],))
    existing_record = cursor.fetchone()
    if not existing_record:  #Se o registro não existe, insere ele no banco de dados
        cursor.execute("INSERT INTO respostas (email, nome, idade, altura, curso, satisfacao) VALUES (?, ?, ?, ?, ?, ?)", 
                       (record['Email'], record['Nome'], record['Qual é a sua idade?'], record["Qual é a sua altura?"], record["Qual é a área do seu curso?"], record["O quanto você está satisfeito com seu curso?"]))

#Salva as mudanças no banco de dados
conn.commit()

# #Consulta simples, servindo mais para testes
cursor.execute("SELECT * FROM respostas")
rows = cursor.fetchall()
for row in rows:
    print(row)

#Fecha a conexão com o banco de dados
conn.close()