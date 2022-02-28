==========MySQL=================

CREATE DATABASE oldtech;

use oldtech;

CREATE TABLE IF NOT EXISTS vendas(
id_venda integer auto_increment primary key,
nota_fiscal integer not null,
vendedor varchar(50) not null,
total decimal(10,2) not null
);


==========Cassandra===============

CREATE KEYSPACE IF NOT EXISTS oldtech
WITH replication = {
    'class':'SimpleStrategy', 'replication_factor': 1};

use oldtech;

CREATE TABLE "oldtech"."vendas" (
    id_venda uuid ,
    nota_fiscal int ,
    vendedor text,
    total float,
    PRIMARY KEY (id_venda, vendedor)
    ) WITH CLUSTERING ORDER BY (vendedor ASC);