import pyodbc
#passamos todos os parametros para conexão com banco de dados
driver = "MySQL ODBC 8.0 ANSI Driver"
server = "aws.connect.psdb.cloud"
database = "NOME DO SEU BANCO"
username = "USUARIO"
password = "SENHA"
string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
conexao = pyodbc.connect(string_conexao)

cursor = conexao.cursor()

#Vamos Para o Crud , no caso no banco de dados ja temos a tabela cadastros com campos id,nome,email
#Create
'''nome=str(input('Digite um Nome para cadastro :')) #danilo    
email=str(input('Digite um email para cadastro :')) #danilo1997@hotmail.com
comando_create = f'INSERT INTO cadastros (nome,email) VALUES ("{nome}","{email}")'
cursor.execute(comando_create)
conexao.commit()#edita banco de dados'''
#Read
'''comando_ler = f'SELECT * FROM cadastros'
cursor.execute(comando_ler)
ler = cursor.fetchall()
print(ler)
cursor.close()
conexao.close()'''
#Update
'''comando_update = f'UPDATE cadastros set email = "danilo1997@hotmail.com" where id = "5"'
cursor.execute(comando_update)
conexao.commit()#edita banco de dados
cursor.close()
conexao.close()'''
#Delete
'''comando_delete = f'DELETE FROM cadastros where nome="Danilo"'
cursor.execute(comando_delete)
conexao.commit()#edita banco de dados
cursor.close()
conexao.close()'''