-- ------------------------- Atividade 09 - Trabalho Python + SQL ------------------------- --
-- Rayssa Melo

-- ---------------------------------------------------------------------------------------- --

-- Esquema Relacional do Banco de dados (Os inserts principais estão em anexo)

-- Fornecedor (idfornecedor, nome, cnpj)
-- Produto (idproduto, idfornecedor, descricao, preco, quantEstoque)
-- Vendedor (idvendedor, nome, cpf, endereco, telefone)
-- Vendas (idvenda, idproduto, idvendedor, valorTotal, comissão)

-- ---------------------------------------------------------------------------------------- --

-- Criando as tabelas no banco de dados e definindo seus atributos

CREATE database DROGARIA_PARAIBANA;
USE DROGARIA_PARAIBANA;
SHOW TABLES;
SELECT * from FORNECEDOR;
SELECT * from VENDEDOR;
SELECT * from  PRODUTO;
SELECT * from vendas;

SELECT valorTotal from vendas;

CREATE table if not exists FORNECEDOR (
	idfornecedor int auto_increment,
    nome long,
    cnpj varchar(25) not null,
    
    constraint fornecedor_pkey primary key (idfornecedor)
);

CREATE table if not exists VENDEDOR (
	idvendedor int auto_increment,
    nome long,
    cpf varchar(25) not null,
    endereco varchar(50),
    telefone long,
    
    constraint vendedor_pkey primary key (idvendedor)
);

CREATE table if not exists PRODUTO (
	idproduto int auto_increment,
    idfornecedor int,
    descricao long,
    preco numeric(10,2),
    quantEstoque numeric(10,2),
    
    constraint produto_pkey primary key (idproduto),
    constraint produto_fkey foreign key(idfornecedor) references fornecedor(idfornecedor)
);

CREATE table if not exists VENDAS (
	idvenda int auto_increment, 
    idproduto int not null, 
    idvendedor int, 
    valorTotal numeric(10,2), 
    comissao numeric(10,2),
    
    constraint vendas_pkey primary key (idvenda),
    constraint vendas_fkey foreign key (idproduto) references produto(idproduto),
    constraint vendas_fkey2 foreign key (idvendedor) references vendedor(idvendedor)
);


