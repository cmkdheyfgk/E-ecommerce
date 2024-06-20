#Cria um novo banco de dados chamado e_commerce.
create database e_commerce;

# Seleciona o banco de dados e_commerce para ser utilizado nas operações seguintes.
use e_commerce;

# Cria uma nova tabela chamada produto com três colunas
create table produto(
id int auto_increment not null primary key, # Um número inteiro autoincrementável que serve como chave primária da tabela 
nome varchar(50) not null,   # Uma string de até 50 caracteres que não pode ser nula
preco DECIMAL(10,2) not null  #  Um número decimal (decimal com 10 dígitos no total e 2 dígitos após o ponto decimal) que não pode ser nulo
); 


# Insere um novo registro na tabela produto com os valores especificados
insert into produto (nome,preco) values ('tenis futsal','500');

#  Seleciona todos os registros da tabela produto e exibe o resultado
select*from produto;


