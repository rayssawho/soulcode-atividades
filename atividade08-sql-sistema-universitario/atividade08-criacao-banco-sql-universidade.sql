#----------------------------- Atividade 08 - SQL ---------------------------------
# Rayssa Melo
# Criação do Banco, criação de tabelas e Inserts.

create database UFPB;
use UFPB;
show databases;
Select * from ALUNO;
Select * from CURSO;
Select * from PROFESSOR;
select * from DISCIPLINAS;
select * from AULA;
select * from matricula;
select * from contem;
SHOW tables;


#Criar a tabela ALUNO 
CREATE TABLE IF NOT EXISTS ALUNO(
	numaluno integer auto_increment,
    nome varchar(50),
    endereco varchar(100),
    cidade varchar(20),
    telefone varchar(13),
    constraint aluno_pkey primary key (numaluno)
);
ALTER TABLE ALUNO ADD COLUMN cursonum integer;
ALTER TABLE ALUNO ADD CONSTRAINT aluno_fkey FOREIGN KEY(cursonum) REFERENCES CURSO(numcurso);
UPDATE ALUNO SET cursonum = 6 WHERE numaluno = 12; 

#constraint matricula_fkey foreign key(numerocurso) references CURSO(numcurso)

insert into ALUNO (nome, endereco, cidade, telefone) values

("Marcos João Casanova","Rua das Casas Velhas","Cidade Nova","83999524523"),
("Ailton Castro", "Rua da felicidade", "João Pessoa", "83956847812"),
("Edvaldo Carlos Silva", "Rua dos lamentos", "Conde", "83985241414"),
("Antônio Lima", "Rua do Canal", "Recife", "81954215248"),
("Joana Alves","Rua da Esperança","Fortaleza","85991256325"),
("Maria Letícia","Rua da Festa","São Luís","98988565423"),
("Rayssa Melo", "Rua da Alegria", "Esperança", "83988245395"),
("Marina Lima", "Rua da Saudade", "João Pessoa", "83996417749"),
("Lucas Emanuel","Rua da inteligência","Patos","83126359875"),
("Maria Eduarda","Rua da Emoção","Itaporanga","83999958751"),
("Paulo Victor", "Rua da Amizade", "São José de Caiana", "83994563125"),
("Vinícius Alcântara","Rua das Novas Palavras","Natal","84998754545");


#Criar a tabela PROFESSOR
CREATE TABLE IF NOT EXISTS PROFESSOR(
	numprof integer auto_increment,
    nome varchar(50),
    areapesquisa varchar(15),
    constraint professor_pkey primary key (numprof)
);

ALTER TABLE PROFESSOR MODIFY areapesquisa varchar(40);
insert into PROFESSOR (nome, areapesquisa) values

("Ramon Travanti", "Humanas"),
("Marcos Salvador", "Exatas e Tecnológicas"),
("Abgair","Saúde"),
("Maria Julia", "Ciências Biológicas"),
("Greiciane Frazão", "Linguística"),
("Adriano Gomes","Exatas e Tecnológicas"),
("Felipe Muylaert","Exatas e Tecnológicas");

#Criar a tabela DISCIPLINAS
CREATE TABLE IF NOT EXISTS DISCIPLINAS(
	numdisp integer auto_increment,
    nome varchar(40),
    quantcreditos integer,
    constraint disciplinas_pkey primary key (numdisp)
);

insert into DISCIPLINAS (nome, quantcreditos) values
("Cálculo Numérico", 4),
("Banco de Dados", 4),
("Engenharia de Software", 4),
("Fotografia", 3),
("Anatomia", 5),
("Metodologia", 4),
("História da Língua Portuguesa", 4),
("Laboratório de Programação", 2),
("Biologia Molecular", 6),
("Metodologia da História", 5),
("Aplicações WEB", 4);

#Criar a tabela CURSO
CREATE TABLE IF NOT EXISTS CURSO(
	totalcreditos integer,
    nome varchar (40),
    numcurso integer auto_increment,
    constraint curso_pkey primary key (numcurso)
);

insert into CURSO (totalcreditos, nome) values
(70, "Ciência da Computação"),
(60,"Comunicação em Mídias Digitais"),
(70,"Nutrição"),
(60,"História"),
(80,"Farmácia"),
(60,"Sistemas para Internet");


CREATE TABLE IF NOT EXISTS MATRICULA(
	numerocurso integer,
    numealuno integer,
    constraint matricula_fkey foreign key(numerocurso) references CURSO(numcurso),
    constraint matricula_fkey2 foreign key(numealuno) references ALUNO(numaluno)
);

INSERT INTO MATRICULA (numerocurso, numealuno) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(2, 5),
(2, 6),
(2, 7),
(3, 8),
(4, 9),
(5, 10),
(6, 11),
(6, 12);

CREATE TABLE IF NOT EXISTS CONTEM(
	cursonumero integer,
    dispnumero integer,
    constraint contem_fkey foreign key(cursonumero) references CURSO(numcurso),
    constraint contem_fkey2 foreign key(dispnumero) references DISCIPLINAS(numdisp)
);

INSERT INTO CONTEM (cursonumero, dispnumero) VALUES
(1, 1),(1, 2),(1, 3),(1, 6),(1, 8),(1, 11),
(2, 4),(2, 6),(2,11),
(3, 5),(3, 6),(3, 9),
(4, 4), (4, 7), (4, 10),
(5, 5),(5, 6),(5, 9),
(6, 1),(6, 2), (6, 3), (6, 6), (6, 8), (6, 11);


CREATE TABLE IF NOT EXISTS AULA(
	semestre varchar(2),
    nota numeric(10,2),
    numeroaluno integer,
    numeroprof integer,
    numerodisp integer,
    constraint aula_fkey foreign key(numeroaluno) references ALUNO(numaluno),
    constraint aula_fkey2 foreign key(numeroprof) references PROFESSOR(numprof),
    constraint aula_fkey3 foreign key(numerodisp) references DISCIPLINAS(numdisp)
);

ALTER TABLE AULA MODIFY nota numeric(10,2);
ALTER TABLE AULA modify semestre varchar(6);

INSERT INTO AULA (semestre, nota, numeroaluno, numeroprof, numerodisp) VALUES
("1998.1", 7.00, 1, 9, 1),("1998.1", 8.00, 1, 13, 2),("1998.1", 6.00, 1, 14, 3),("1998.1", 8.00, 1, 12, 6),("1998.1", 7.00, 1, 14, 8),("1998.1", 7.00, 1, 9, 11),
("1998.1", 4.00, 2, 9, 1),("1998.1", 5.00, 2, 13, 2),("1998.1", 7.00, 2, 14, 3),("1998.1", 3.00, 2, 12, 6),("1998.1", 3.00, 2, 14, 8),("1998.1", 4.00, 2, 9, 11),
("1998.1", 7.00, 3, 9, 1),("1998.1", 7.50, 3, 13, 2),("1998.1", 8.00, 3, 14, 3),("1998.1", 6.00, 3, 12, 6),("1998.1", 7.00, 3, 14, 8),("1998.1", 8.00, 3, 9, 11),
("1998.1", 4.00, 4, 9, 1),("1998.1", 5.00, 4, 13, 2),("1998.1", 7.00, 4, 14, 3),("1998.1", 6.00, 4, 12, 6),("1998.1", 3.00, 4, 14, 8),("1998.1", 5.00, 4, 9, 11),

("1998.1", 9.00, 5, 8, 4),("1998.1", 10.00, 5, 12, 6),("1998.1", 8.00, 5, 9, 11),
("2000.1", 8.00, 6, 8, 4), ("2000.1", 9.00, 6, 12, 6), ("2000.1", 8.00, 6, 9, 11),
("2010.2", 8.00, 7, 8, 4),("2010.2", 9.00, 7, 12, 6),("2010.2", 7.00, 7, 9, 11),

("2005.2", 7.00, 8, 10, 5),("2005.2", 8.00, 8, 10, 9),("2005.2", 7.00, 8, 12, 6),

("1992.2", 8.00, 9, 8, 4),("1992.2", 9.00, 9, 8, 7),("1992.2", 10.00, 9, 12, 10),

("2006.1", 9.00, 10, 10, 5),("2006.1", 8.00, 10, 12, 6),("2006.1", 7.00, 10, 10, 9),

("1997.1", 8.00, 11, 9, 1),("1997.1", 7.00, 11, 13, 2),("1997.1", 8.00, 11, 14, 3),("1997.1", 6.00, 11, 12, 6),("1997.1", 7.00, 11, 14, 8),("1997.1", 9.00, 11, 9, 11),
("1997.1", 9.00, 12, 9, 1),("1997.1", 9.00, 12, 13, 2),("1997.1", 10.00, 12, 14, 3),("1997.1", 10.00, 12, 12, 6),("1997.1", 9.00, 12, 14, 8),("1997.1", 10.00, 12, 9, 11)
;