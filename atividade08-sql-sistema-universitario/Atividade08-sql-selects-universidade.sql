#----------------------------- Atividade 08 - SQL ---------------------------------
# Rayssa Melo
# SELECTS

#5. Quais os nomes das disciplinas do curso de Ciência da Computação?
select disciplinas.nome from contem inner join curso on curso.numcurso = contem.cursonumero join disciplinas on disciplinas.numdisp = 
contem.dispnumero where curso.nome = "Ciência da Computação";


#6. Quais os nomes dos cursos que possuem no curriculum a disciplina Cálculo Numérico?
SELECT curso.nome from contem inner join curso on curso.numcurso = contem.cursonumero join disciplinas on disciplinas.numdisp = 
Contem.dispnumero where disciplinas.nome ="Cálculo Numérico";


#7. Quais os nomes das disciplinas que o aluno Marcos João Casanova cursou no 1o semestre de 1998?
SELECT disciplinas.nome, aluno.nome from aula inner join aluno on aluno.numaluno join disciplinas on disciplinas.numdisp = aula.numerodisp where 
aluno.nome = "Marcos João Casanova" and aula.numeroaluno = 1;


#8. Quais os nomes de disciplinas que o aluno Ailton Castro foi reprovado?
SELECT disciplinas.nome, aluno.nome from aula inner join aluno on aluno.numaluno join disciplinas on disciplinas.numdisp = aula.numerodisp where 
aluno.nome = "Ailton Castro" and aula.numeroaluno = 2 and aula.nota < 7.00;


#9. Quais os nomes de alunos reprovados na disciplina de Cálculo Numérico no 1º semestre de 1998?
SELECT aluno.nome from aula inner join aluno on aluno.numaluno = aula.numeroaluno join disciplinas on disciplinas.numdisp = 
aula.numerodisp where disciplinas.nome = "Cálculo Numérico" and aula.nota < 7;


#10. Quais os nomes das disciplinas ministradas pelo prof. Ramon Travanti?
SELECT disciplinas.nome from aula inner join professor on Professor.numprof = aula.numeroprof join disciplinas on 
disciplinas.numdisp = aula.numerodisp where professor.nome = "Ramon Travanti";


#11. Quais os nomes dos professores que já ministraram aula de Banco de Dados?
SELECT professor.nome, disciplinas.nome from aula inner join disciplinas on disciplinas.numdisp = aula.numerodisp join professor on
professor.numprof = aula.numeroprof where aula.numerodisp = 2;


#12. Qual a maior e a menor nota na disciplina de Cálculo Numérico no 1º semestre de 1998?
SELECT max(aula.nota), min(aula.nota) from aula join disciplinas on disciplinas.numdisp = aula.numerodisp
where disciplinas.nome = "Cálculo Numérico" and aula.semestre = "1998.1"; 


#13. Qual o nome do aluno e nota que obteve maior nota na disciplina de Engenharia de Software no 1º semestre de 1998?
SELECT aluno.nome, max(aula.nota), disciplinas.nome from AULA Join aluno On aluno.numaluno = aula.numeroaluno Join disciplinas 
On disciplinas.numdisp = aula.numerodisp where disciplinas.nome = "Engenharia de Software" and aula.semestre = "1998.1";


#14. Quais os nomes de alunos, nome de disciplina e nome de professores que cursaram o 1º semestre de 1998 em ordem de aluno?
SELECT aluno.nome, disciplinas.nome, professor.nome from aula Join aluno on aluno.numaluno = aula.numeroaluno join disciplinas 
on disciplinas.numdisp = aula.numerodisp join professor on professor.numprof = aula.numeroprof where aula.semestre = "1998.1" order by aluno.nome;


#15. Quais os nomes de alunos, nome de disciplina e notas do 1º semestre de 1998 no curso de Ciência da Computação?
SELECT aluno.nome, disciplinas.nome, aula.nota from aula inner join aluno on aluno.numaluno = aula.numeroaluno join disciplinas on 
disciplinas.numdisp = aula.numerodisp join curso on curso.numcurso = aluno.cursonum where aula.semestre = "1998.1" and curso.nome = "Ciência da Computação";


#16. Qual a média de notas do professor Marcos Salvador?
SELECT avg(aula.nota), professor.nome from aula inner join aluno on aluno.numaluno = aula.numeroaluno Join disciplinas on disciplinas.numdisp =
aula.numerodisp join professor on professor.numprof = aula.numeroprof where professor.nome = "Marcos Salvador" order by professor.nome;


#17. Quais nomes de alunos, nomes de disciplinas e notas que tiveram nota entre 5.0 e 7.0 em ordem de disciplina?
SELECT aluno.nome, disciplinas.nome, aula.nota from aula inner join aluno on aluno.numaluno = aula.numeroaluno join disciplinas on disciplinas.numdisp =
aula.numerodisp where aula.nota > 5.00 and aula.nota < 7.00;


#18. Qual a média de notas da disciplina Cálculo Numérico no 1º semestre de 1998?
SELECT avg(aula.nota), disciplinas.nome from aula inner join disciplinas on disciplinas.numdisp = aula.numerodisp where aula.semestre = "1998.1" and aula.numerodisp = 1;

#----------para testar se funciona-----------------
#SELECT (aula.nota), disciplinas.nome from aula inner Join disciplinas on disciplinas.numdisp = aula.numerodisp where aula.semestre = "1998.1" and aula.numerodisp = 1;


#19. Quantos alunos o professor Abgair teve no 1º semestre de 1998?
SELECT count(aluno.nome), professor.nome from aula inner join aluno on aluno.numaluno = aula.numeroaluno join professor on professor.numprof = 
aula.numeroprof where professor.nome = "Abgair";


#20. Qual a média de notas do aluno Edvaldo Carlos Silva?
SELECT avg(aula.nota), aluno.nome from aula inner join aluno on aluno.numaluno = aula.numeroaluno where aluno.nome = "Edvaldo Carlos Silva"; 

#----------para testar se funciona-----------------
#SELECT aula.nota, aluno.nome from aula inner join aluno on aluno.numaluno = aula.numeroaluno where aluno.nome = "Edvaldo Carlos Silva"; 


#21. Quais as médias por nome de disciplina de todos os cursos do 1º semestre de 1998 em ordem de disciplina?
SELECT disciplinas.nome, avg(aula.nota) as MEDIA from aula inner join aluno on aluno.numaluno = aula.numeroaluno join disciplinas on 
disciplinas.numdisp = aula.numerodisp where aula.semestre = "1998.1" group by disciplinas.nome;


#22. Quais as médias das notas por nome de professor no 1º semestre de 1998?
SELECT professor.nome, avg(aula.nota) as MEDIA from aula inner join aluno on aluno.numaluno = aula.numeroaluno join professor on 
professor.numprof = aula.numeroprof where aula.semestre = "1998.1" group by professor.nome;


#23. Qual a média por disciplina no 1o semestre de 1998 do curso do Ciência da Computação?
SELECT curso.nome, disciplinas.nome, avg(aula.nota) as MEDIA from aula inner join aluno on aluno.numaluno = aula.numeroaluno join disciplinas 
on disciplinas.numdisp = aula.numerodisp join curso on curso.numcurso = aluno.cursonum WHERE aula.semestre = "1998.1" 
and curso.nome = "Ciência da Computação" GROUP BY disciplinas.nome;


#24. Qual foi quantidade de créditos concluídos (somente as disciplinas aprovadas) do aluno Edvaldo Carlos Silva?
SELECT SUM(disciplinas.quantcreditos) FROM aula inner join aluno on aluno.numaluno = aula.numeroaluno join disciplinas on disciplinas.numdisp 
= aula.numerodisp where aluno.nome = "Edvaldo Carlos Silva" and Aula.nota >= 7;


#26. Quais nomes de alunos, nome de disciplina e nome de professores que cursaram o 1º semestre de 1998 e pertencem ao curso 
#de ciência da Computação que possuem nota superior à 8.0?
SELECT aluno.nome, disciplinas.nome, professor.nome from aula inner join aluno on aluno.numaluno = aula.numeroaluno join disciplinas on 
disciplinas.numdisp = aula.numerodisp join professor on professor.numprof = aula.numeroprof JOIN curso on curso.numcurso = 
Aluno.cursonum where aula.semestre = "1998.1" and curso.nome = "Ciência da Computação" and aula.nota > 8.00 GROUP BY aluno.nome;

#------------------não apareceu nenhum, pois nenhum aluno conseguiu tirar mais que 8.00 no curso de Ciência da Computação-------------------


#27 Qual a disciplina com nota mais baixa em qualquer época?
SELECT disciplinas.nome, Min(aula.nota) from aula inner join aluno on aluno.numaluno = aula.numeroaluno join disciplinas on disciplinas.numdisp = 
aula.numerodisp;


#28. Qual a disciplina com média de nota mais alta em qualquer época?
SELECT disciplinas.nome, avg(aula.nota) as MEDIA from aula inner join aluno on aluno.numaluno = aula.numeroaluno join disciplinas on 
disciplinas.numdisp = aula.numerodisp GROUP BY disciplinas.nome 
LIMIT 1;


#29. Quais alunos já concluiram o curso de Ciência da Computação?
SELECT aluno.nome, SUM(disciplinas.quantcreditos) = curso.totalcreditos as 
"FORMANDOS = 1" from aula inner join aluno on aluno.numaluno = Aula.numeroaluno join disciplinas on disciplinas.numdisp = 
Aula.numerodisp join curso on curso.numcurso = Aluno.cursonum where aula.nota >= 7 group by aluno.nome;


#30. Ordene as disciplinas por quantidade de reprovações:
SELECT disciplinas.nome, COUNT(disciplinas.nome) as REPROVADOS from Aula inner join aluno on aluno.numaluno = aula.numeroaluno join disciplinas on 
disciplinas.numdisp = aula.numerodisp where aula.nota < 7 group by disciplinas.nome order by disciplinas.nome desc;




