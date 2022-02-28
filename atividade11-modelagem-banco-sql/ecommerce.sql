create database ecommerce;
use ecommerce;

/*
Cliente(idCliente, nome, cpf, telefone, endereco)
Produto(idProduto, nome, disponibilidade, descricao, preco_unitario)
Estoque(idProduto, qtde)
Pedido(idPedido, idCliente, idProduto, quant, total)
Entrega(idPedido, data_envio)
*/

create table if not exists cliente(
	idCliente int not null auto_increment,
    nome long not null,
    cpf varchar(15) not null,
	telefone varchar(15) not null,
    endereco varchar(100) not null, 
    #primary key
    constraint cliente_pkey primary key (idCliente)
); 

create table if not exists produto(
	idProduto int not null auto_increment,
    nome long not null,
    disponibilidade char(1) not null, #Existe produto disponivel ? Se sim, S, se não N.
    descricao varchar(50) not null, 
    preco_unitario float not null,
    #primary key
    constraint produto_pkey primary key (idProduto)
); 

create table if not exists estoque(
    idProduto int not null, 
    qtde int not null, 
    #primary key
    constraint estoque_pkey primary key (idProduto),
    #foreign key
    constraint estoque_fkey_produto foreign key (idProduto) references produto(idProduto)
); 

create table if not exists pedido(
	idPedido int not null,
    idCliente int not null,
    idProduto int not null,
    quant int not null,
    total float not null, 
    #foreign key
    constraint pedido_fkey_cliente foreign key (idCliente) references cliente(idCliente),
	constraint pedido_fkey_produto foreign key (idProduto) references produto(idProduto)
); 

create table if not exists entrega(
    idPedido int not null,
	data_envio varchar(20) not null 
); 

insert into cliente (nome, cpf, telefone, endereco) values 
("João","123.456.789-10","(32)12345-6789","Rua X"),
("Rayssa","987-654-321-99","(83)98765-4321","Rua Y"),
("Fátima","154.256.985-23","(11)98562-1514","Rua Z");

insert into produto (nome, disponibilidade, descricao, preco_unitario) values 
("Caixa de som","S","JBL C3000",2999.90),
("Mouse","S","Razer JB234",49.90),
("Teclado","S","Multilaser S380",69.90),
("Iphone","N","XR",5999.99);

insert into estoque (idProduto, qtde) values (1,5),(2,65),(3,82),(4,0);

#procedure para inserir um dado na tabela Entrega
delimiter //
create procedure sp_InsereEntrega (in idPed int)
	begin
		 insert into entrega (idPedido, data_envio) values (idPed, CURRENT_TIMESTAMP );
	end
//

#procedure para deletar um dado da tabela Entrega
delimiter //
create procedure sp_DeleteEntrega (in idPed int)
	begin
		delete from entrega where idPedido = idPed;
	end
//

#trigger incluindo pedido (diminui a quantidade em estoque)
delimiter //
CREATE TRIGGER trg_Pedido_Insert_AI AFTER INSERT ON pedido
	FOR EACH ROW
		BEGIN
			UPDATE Estoque SET qtde = qtde - New.quant WHERE idProduto = New.idProduto;
			UPDATE Produto SET disponibilidade = "N" WHERE idProduto = (select idProduto from estoque where new.idProduto = idProduto and qtde = 0);
            call sp_InsereEntrega(new.idPedido);
		END
//

#trigger deletando pedido (se o pedido foi extornado, aumenta a quantidade em estoque)
delimiter //
CREATE TRIGGER trg_Pedido_Delete_AD AFTER DELETE ON pedido
	FOR EACH ROW
		BEGIN
			UPDATE Estoque SET qtde = qtde + Old.quant WHERE idProduto = Old.idProduto;
			call sp_DeleteEntrega (old.idPedido);
		END 
//

#trigger para atualizar o estoque (adicionar novos produtos para serem vendidos)
delimiter //
CREATE TRIGGER trg_Estoque_Update_AU AFTER UPDATE ON estoque
	FOR EACH ROW
		BEGIN
			UPDATE Produto SET disponibilidade = "S" WHERE idProduto = new.idProduto;
        END;
//

insert into pedido (idPedido, idCliente, idProduto, quant, total) values (1, 2, 1, 3, 8999.7),(1, 2, 2, 10, 499.0);
insert into pedido (idPedido, idCliente, idProduto, quant, total) values (2, 1, 1, 2, 5999.8),(2, 1, 3, 2, 138.9);
insert into pedido (idPedido, idCliente, idProduto, quant, total) values (3, 3, 2, 10, 499.0);

delete from pedido where idPedido = 3;

update estoque set qtde = 10 where idProduto = 1;

insert into pedido (idPedido, idCliente, idProduto, quant, total) values (3, 3, 1, 10, 29998.0);

select * from cliente;
select * from produto;
select * from estoque;
select * from pedido;
select * from entrega;