# Aqui, estamos importando o módulo mysql.connector, que é
#  utilizado para a conexão e interação com o banco de dados
#  MySQL
import mysql.connector


# Definimos a classe Produto, que possui dois atributos: nome e preco.
# Essa classe serve para representar os produtos que serão manipulados
# no sistema de e-commerce
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


# A classe SistemaDeEcommerce é onde ocorre a conexão com o banco de dados MySQL.
#  No método __init__, conectamos ao banco utilizando as credenciais especificadas
#  (host, usuário, senha e nome do banco de dados) e inicializamos para no executar  SQL
class SistemaDeEcommerce:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="e_commerce"
        )
        self.cursor = self.conexao.cursor()


# No método adicionar_produto, inserimos um novo produto na tabela produto do banco
# de dados. Utilizamos SQL parametrizado , passando os valores
# do produto (nome e preco) como parâmetros. Após executar a inserção, fazemos o commit
# para confirmar a transação no banco de dados


    def adicionar_produto(self, produto):
        # Adiciona um produto ao banco de dados.
        sql = "INSERT INTO produto (nome,preco) VALUES (%s, %s)"
        valores = (produto.nome, produto.preco)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('produto adicionado.')


# O método listar_produto executa uma consulta SQL simples para selecionar todos os produtos
#  na tabela produto. Em seguida, percorremos os resultados com um loop for e imprimimos o
# nome e o preço de cada produto


    def listar_produto(self):
        self.cursor.execute("SELECT nome,preco FROM produto")
        produto = self.cursor.fetchall()
        for produto in produto:
            print(f"nome:{produto[0]}, preco: {produto[1]}")


# O método fechar_conexao fecha tanto o cursor quanto a conexão com o banco de dados, garantindo
#  que todos os recursos sejam liberados corretamente


    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()


sistema = SistemaDeEcommerce()

nome = input('nome do produto:')
preco = input('preco do produto: R$')
estoque = Produto(nome, preco)
sistema.adicionar_produto(estoque)


print('produtos:')
sistema.listar_produto()

sistema.fechar_conexao()


# Neste trecho final do código, criamos uma instância sistema da classe SistemaDeEcommerce.
# Em seguida, solicitamos ao usuário que insira o nome e o preço de um produto, criamos um
# objeto Produto com esses valores e adicionamos esse produto ao banco de dados utilizando o
# método adicionar_produto do objeto sistema. Após adicionar o produto, listamos todos os produtos
# do banco de dados usando listar_produto e, por fim, fechamos a conexão com o banco de dados usando fechar_conexao.
