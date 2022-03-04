# Atividade 06
Criação de um banco de dados no MySQL. Comandos SQL - DDL.

## Proposta

Analisar o DER da clínica BOA SAUDE. /

Foi apresentado um modelo relacional /

* Paciente(codpac, nome, endereço, telefone) 
* Medico(crm, nome, endereço, telefone, especialidade) 
* Convenio(codconv, nome) 
* Consulta(codconsulta, data, horário, medico, paciente, convenio, porcent) 
* Atende(medico, convenio) 
* Possui(paciente, convenio, tipo, vencimento) /

A seguir foi apresentado um simples dicionário de dados onde é descrito o significado de cada atributo  de cada relação. Defina qual tipo de dado é o ideal para cada atributo. Após, implemente o banco  BOASAUDE no POSTGREESQL, MySQL ou SGBD Equivalente. /

Mais detalhes no arquivo: *descricao_atividade06.pdf*

Execute os comandos abaixo: 

1. Atualize o endereço do paciente João para ‘Rua do Bonde’; 
2. Atualize os dados do medico Elias para ‘Rua Z’ e telefone ‘9838-7867’; 
3. Atualize todos os tipos dos convênios que os pacientes possuem para ‘S’; 
4. Exclua a informação que o paciente José tem o convenio 232; 
5. Exclua a consulta realizada do dia 14/05/2013 as 14:00.
6. Altere o nome da coluna especialidade, da tabela médico, para especialização. 7. Altere o tipo de dado da coluna nome, da tabela convenio, para varchar(200). 8. Acrescente a coluna Valor na tabela consulta e atualize todas as consultas para o valor de  R$100,00.


## Tecnologias utilizadas

* MySQL



## Autor

* [Rayssa Alcântara](https://www.linkedin.com/in/rayssarte/) 
