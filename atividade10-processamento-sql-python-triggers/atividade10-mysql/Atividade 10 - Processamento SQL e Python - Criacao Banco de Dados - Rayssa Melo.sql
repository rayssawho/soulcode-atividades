-- Atividade 10 - Processamento SQL e Python
-- ------------------------------------------------------

CREATE DATABASE AULA_17_11_21;
USE AULA_17_11_21;

create table if not exists PRODUTOS(
	referencia varchar(3) primary key,
    descricao varchar(60) UNIQUE,
    Estoque int not null default 0
);

CREATE TABLE IF NOT EXISTS ITENSVENDA(
venda int,
produto varchar(3),
quantidade int
);

INSERT INTO ITENSVENDA values (1, "025", 3);

-- -----------------------------------------------------
-- TRIGGER INSERINDO VENDAS
-- -----------------------------------------------------

DELIMITER $
CREATE TRIGGER tgr_ItensVenda_Insert AFTER INSERT ON ItensVenda
	FOR each row
		BEGIN
			UPDATE Produtos SET Estoque = Estoque - New.quantidade WHERE Referencia = New.Produto;
		END$
        
-- -----------------------------------------------------
-- TRIGGER EXCLUINDO VENDAS
-- -----------------------------------------------------
	     
CREATE TRIGGER tgr_ItensVenda_Delete AFTER DELETE ON ItensVenda
FOR each row
	BEGIN
		UPDATE Produtos SET Estoque = Estoque + OLD.quantidade WHERE referencia = OLD.produto;
	END$
    
DELIMITER ; 


drop TRIGGER tgr_ItensVenda_Insert;
drop trigger tgr_ItensVenda_Delete;

INSERT INTO produtos  VALUES
 ("001", "Arroz", 35), 
("005", "Feijão", 89), 
("152", "Fragrância Masculina", 98),
("002", "alface", 50),
("016", "Chocolate", 100),
("032", "Macarrao", 121),
("007", "Leite em pó", 40),
("006", "nuggets", 40),
("027", "farinha", 40),
("020", "Rúcula", 35),
("035", "tomate", 325),
("747","Aveia",70),
("300", "chimia", 30),
("050","Cup Noodles",60),
("009", "Pão de forma", 20),
("998", "Macaxeira", 99),
("084", "Mandioca",70),
("112", "Caju", 100),
("245", "Açaí", 50),
("200","bergamota",20),
("113", "abacate", 15),
("115", "queijo", 25),
("333", "Cuscuz", 100),
("543", "Tapioca", 60),
("302", "Brócolis", 20),
("666", "Coca-Cola", 100),
("045", "Pão de Queijo", 40);
