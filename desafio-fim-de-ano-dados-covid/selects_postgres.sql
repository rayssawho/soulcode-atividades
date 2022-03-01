select count(*) from covid_data;

select * from covid_data;

-- Primeiro registro de óbitos em um BD
select date, location, total_cases, total_deaths from covid_data
where location = 'China' and date = '2020-01-22';

-- Registro de casos e óbitos na Ásia e Estados Unidos nessa mesma data
select location, date, total_cases, total_deaths from covid_data
where date = '2020-01-22';

-- Casos e Óbitos no MUNDO quando a OMS declarou uma Pandemia Mundial em Março de 2020
select location, date, total_cases, total_deaths from covid_data 
where location = 'World' and date = '2020-03-11';

-- Data da Primeira morte no BRASIL
select location, date, total_cases, total_deaths from covid_data 
where location = 'Brazil' order by date;

-- 'País com maior número de casos em 2020'
select total_cases, location from covid_data
where date = '2020-12-31' order by total_cases desc;

-- 'Qual foi o país que mais vacinou até Janeiro 2022'
select date,total_vaccinations,location from covid_data 
where date = '2022-01-01' order by total_vaccinations desc;

-- 'Maior Nº de casos em um dia no Brasil'
select max(cd.new_cases) from covid_data cd
where cd.location = 'Brazil';

select date, new_cases from covid_data where location = 'Brazil' order by new_cases desc;

-- Maior Nº de óbitos em um dia no Brasil e no Mundo'
select date, new_deaths, location from covid_data 
where location = 'Brazil' order by new_deaths desc;

select date, new_deaths, location from covid_data
where location = 'World' order by new_deaths desc;

-- Data primeira Vacina no Brasil
select date ,new_vaccinations from covid_data 
where location = 'Brazil';

-- Total de vacinação no mundo
select total_vaccinations from covid_data where date = '2022-01-01' order by total_vaccinations

-- Havia casos em quantos países quando a OMS declarou Pandemia?
select location, date, total_cases from covid_data where date = '2020-03-11'

-- Data em que a COVID se espalhou por todos os estados Brasileiros e DF, e quantidas de mortes nessa data
select total_cases,total_deaths,location, date from covid_data where date = '2020-03-24' and location = 'Brazil'


-- Total de Casos no Ano de 2020 no MUNDO
select location, total_cases, total_tests, date from covid_data where location = 'World' and date = '2020-12-31'

-- Total de Casos no Ano de 2020 no BRASIL
select location, total_cases, total_tests, date from covid_data where location = 'Brazil' and date = '2020-12-31'

-- Total de Casos e testes no Ano de 2020 nos USA
select location, total_cases, total_tests, date from covid_data where location = 'United States' and date = '2020-12-31'


-- Quantidade de casos em Agosto de 2020
select location ,new_cases, new_deaths from covid_data
where location = 'Brazil' and date = '2020-12-31'      1016 óbitos

-- Quantidade de casos em Agosto de 2021
select location ,new_cases, new_deaths from covid_data
where location = 'Brazil' and date = '2021-12-31'      85 óbitos