#create database CLINICA_BOA_SAUDE;
USE CLINICA_BOA_SAUDE;
select * from PACIENTE;
select * from MEDICO;
select * from CONSULTA;
select * from CONVENIO;
select * from ATENDE;
select * from POSSUI;

CREATE TABLE IF NOT EXISTS PACIENTE(
	codpac integer auto_increment,
    nome varchar(60) not null,
    endereco varchar(100) not null,
    telefone varchar(14) not null,
    constraint paciente_pkey primary key (codpac)
);
CREATE TABLE IF NOT EXISTS MEDICO(
	crm varchar(10) not null,
    nome varchar(60) not null,
    endereco varchar(100) not null,
    telefone varchar(14) not null,
    especialidade varchar(30) not null,
    constraint medico_pkey primary key (crm)
);
CREATE TABLE IF NOT EXISTS CONVENIO(
	codconv integer not null,
    nome varchar(20) not null,
    constraint convenio_pkey primary key (codconv)
);

CREATE TABLE IF NOT EXISTS CONSULTA(
	codconsulta integer auto_increment,
    dataconsulta varchar(10) not null,
    horario varchar(10) not null,
    crmmedico varchar(10),
    codpaciente integer,
    codconvenio integer,
    porcent varchar(10) not null,
    constraint consulta_pkey primary key (codconsulta),
    
    constraint consulta_fkey foreign key(crmmedico) references MEDICO(crm),
    constraint consulta_fkey2 foreign key(codpaciente) references PACIENTE(codpac),
    constraint consulta_fkey3 foreign key(codconvenio) references CONVENIO(codconv)
);

CREATE TABLE IF NOT EXISTS ATENDE(
	crm varchar(10),
    codconv integer,
    
    constraint atende_pkey PRIMARY KEY (crm, codconv),
    
    constraint atende_fkey foreign key(crm) references MEDICO(crm),
    constraint atende_fkey2 foreign key(codconv) references CONVENIO(codconv)
);

CREATE TABLE IF NOT EXISTS POSSUI(
	codpac integer,
    codconv integer,
    tipo char(2),
    vencimento varchar(10),
    
    constraint possui_pkey primary key (codpac, codconv),
    constraint possui_fkey foreign key (codpac) references PACIENTE(codpac),
    constraint possui_fkey2 foreign key (codconv) references CONVENIO(codconv)
);

insert into PACIENTE (nome, endereco, telefone ) values 
("João","Rua 1 ","9809-9756"),
("José ","Rua B ","3621-8978"),
("Maria ","Rua 10 ","4567-9872"),
("Joana ","Rua J ","3343-9889");

insert into MEDICO (crm, nome, endereco, telefone, especialidade) values

("18739 ","Elias ","Rua X ","8738-1221 ","Pediatria"),
("7646 ","Ana ","Av Z ","7829-1233 ","Obstetricia"),
("39872 ","Pedro ","Tv H ","9888-2333 ","Oftalmologia");

insert into CONVENIO (codconv, nome) values
("189 ","Cassi"),
("232 ","Unimed"),
("454 ","Santa Casa"),
("908 ","Copasa"),
("435 ","São Lucas");

insert into CONSULTA (dataconsulta, horario, crmmedico, codpaciente, codconvenio, porcent) values
("10/05/2013 ","10:00 ","18739 ","1 ","189 ","5"),
("12/05/2013 ","10:00 ","7646 ","2 ","232 ","10"),
("12/05/2013 ","11:00 ","18739 ","3 ","908 ","15"),
("13/05/2013 ","10:00 ","7646 ","4 ","435 ","13"),
("14/05/2013 ","13:00 ","7646 ","2 ","232 ","10"),
("14/05/2013 ","14:00 ","39872 ","1 ","189 ","5");  

insert into POSSUI (codpac, codconv, tipo, vencimento) values
("1", "189", "E", "31/12/2016"),
("2", "232", "S", "31/12/2014"),
("3", "908", "S", "31/12/2017"),
("4", "435", "E", "31/12/2016"),
("1", "232", "S", "31/12/2015");

UPDATE PACIENTE SET endereco = "Rua da Lua" WHERE codpac = 5;
UPDATE MEDICO SET ENDERECO = "Rua Z", TELEFONE = "9838-7867" WHERE CRM = 18739;
UPDATE POSSUI SET TIPO = "S";
DELETE FROM POSSUI WHERE codpac = 2;
DELETE FROM CONSULTA WHERE horario = "14:00 ";
ALTER TABLE MEDICO RENAME COLUMN especialidade TO especializacao;
ALTER TABLE CONVENIO MODIFY NOME VARCHAR(200);

ALTER TABLE CONSULTA ADD COLUMN VALOR VARCHAR(8);
UPDATE CONSULTA SET VALOR = "100,00";











