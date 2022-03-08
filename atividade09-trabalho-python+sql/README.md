# Atividade 09
Trabalho Python + SQL



## Proposta

Esquema Relacional do Banco de dados:

- Fornecedor (idfornecedor, nome, cnpj)
- Produto (idproduto, idfornecedor, descricao, preco, quantEstoque)
- Vendedor (idvendedor, nome, cpf, endereco, telefone)
- Vendas (idvenda, idproduto, idvendedor, valorTotal, comissão)

Devem ser realizadas (via query/Python) no mínimo 50 vendas envolvendo produtos e vendedores diversos e apresentar os SELECT's que respondam as questões a seguir:


Crie tabelas e insira dados conforme pedido, via Python responda:

- o total de vendas
- o funcionário que realizou a maior venda e qual o total desta
- o funcionário que realizou a maior quantidade de vendas e quantas foram
- o fornecedor mais utilizado
- o total de comissão devido a cada funcionário considerando-se 8% de comissão


## Tecnologias utilizadas

* Python:
Utilizado para conexão com o banco de dados, inserção de dados e realizar determinadas consultas.


* MySQL
Utilizado para criação da base de dados, criação de tabelas e inserção de dados. 

## Autor

* [Rayssa Alcântara](https://www.linkedin.com/in/rayssarte/) 
