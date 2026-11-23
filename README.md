# Meu desempenho
Protótipo inicial da plataforma descrita no relatório da EduFuturo Tecnologia Educacional.

## Funcionalidades desta versão
- Cadastro e login individual de alunos.
- Associação do cadastro a uma escola informada pelo aluno.
- Cadastro de disciplinas pelo próprio aluno.
- Registro, edição e exclusão de provas e atividades.
- Notas de 0 a 10 organizadas em quatro bimestres.
- Média aritmética simples por bimestre; todas as avaliações têm o mesmo peso.
- Soma das médias bimestrais para acompanhar a meta anual inicial de 24 pontos.
- Painel com pontuação e gráficos simples por disciplina.
- Sem controle de faltas/frequência. Menções não implementadas (ainda).

## Regra de cálculo
A média bimestral é a soma das notas cadastradas no bimestre dividida pela quantidade de avaliações cadastradas. A pontuação anual atual é a soma das médias dos bimestres que já possuem avaliações. O sistema mostra quantos pontos faltam para chegar a 24, sem apresentar valor negativo. Um bimestre sem avaliações fica como “Sem notas”, não como zero.

A indicação é um acompanhamento com base nos dados informados pelo aluno, não uma declaração oficial de aprovação ou reprovação.

## Requisitos
Python 3.10 ou superior.

## Executar no Windows
```powershell
py -m pip install -r requirements.txt
py app.py
```

## Banco de dados
O projeto usa SQLite por padrão. O arquivo do banco será criado automaticamente na pasta `instance/` após iniciar a aplicação.

## Observações
Não publique o sistema usando a chave secreta padrão.
