📚 Meu Desempenho

Sistema web para acompanhamento do desempenho escolar dos alunos.

Desenvolvido com Python, Flask, SQLite, HTML, CSS e JavaScript.

---

📌 Sumário

- "Sobre o projeto" (#-sobre-o-projeto)
- "Funcionalidades" (#-funcionalidades)
- "Tecnologias utilizadas" (#-tecnologias-utilizadas)
- "Instalação e execução" (#-instalação-e-execução)
- "Colaboração no projeto" (#-colaboração-no-projeto)
- "Principais comandos do Git" (#-principais-comandos-do-git)
- "Banco de dados" (#-banco-de-dados)
- "Repositório oficial" (#-repositório-oficial)

---

🎯 Sobre o projeto

O Meu Desempenho é uma plataforma que permite aos alunos registrar e acompanhar suas notas escolares.

O objetivo é facilitar a visualização do desempenho durante os quatro bimestres, permitindo que o estudante acompanhe suas médias e sua evolução ao longo do ano letivo.

⚙️ Funcionalidades

- Cadastro e login de alunos.
- Cadastro de disciplinas.
- Registro de notas de provas e atividades.
- Organização das avaliações por disciplina e bimestre.
- Edição e exclusão de avaliações.
- Cálculo automático das médias.
- Acompanhamento da meta anual de 24 pontos.
- Visualização do desempenho escolar.

💻 Tecnologias utilizadas

Tecnologia| Finalidade
Python| Linguagem principal
Flask| Desenvolvimento da aplicação web
Flask-SQLAlchemy| Integração com o banco de dados
SQLite| Armazenamento das informações
HTML| Estrutura das páginas
CSS| Estilização do sistema
JavaScript| Funcionalidades e interações
Git e GitHub| Controle de versões e colaboração

---

🚀 Instalação e execução

1. Pré-requisitos

Antes de começar, é necessário ter instalado:

- Python
- Git

Verifique se o Python está instalado:

python --version

2. Baixar o projeto

Clone o repositório:

git clone https://github.com/uCezar/Meu-Desempenho.git

Entre na pasta:

cd Meu-Desempenho

3. Instalar as dependências

pip install -r requirements.txt

4. Executar a aplicação

python app.py

Após iniciar o servidor Flask, abra o navegador e acesse:

http://127.0.0.1:5000

«Observação: o banco de dados SQLite é criado automaticamente pela aplicação quando ela é iniciada, conforme a configuração do projeto.»

---

🤝 Colaboração no projeto

Para participar do desenvolvimento, é necessário:

1. Ter uma conta no GitHub.
2. Receber um convite de colaboração do responsável pelo repositório.
3. Aceitar o convite.

O responsável pode enviar o convite acessando:

GitHub → Repositório → Settings → Collaborators → Add people.

1. Baixar o projeto pela primeira vez

Instale o Git e execute:

git clone https://github.com/uCezar/Meu-Desempenho.git

Depois, entre na pasta:

cd Meu-Desempenho

O comando "git clone" baixa os arquivos e configura a conexão com o repositório remoto.

2. Configurar o Git

Cada colaborador deve configurar seu nome e e-mail uma única vez por instalação do Git:

git config --global user.name "Seu Nome"

git config --global user.email "seuemail@exemplo.com"

Essas informações identificam quem realizou cada commit.

3. Atualizar o projeto antes de trabalhar

Antes de começar a fazer alterações, execute:

git pull

Esse comando recebe e integra as atualizações disponíveis no GitHub.

4. Registrar as alterações

Depois de modificar ou criar arquivos, execute:

git add .

Em seguida, registre as alterações:

git commit -m "Descrição das alterações"

Exemplo:

git commit -m "Adicionando tela de cadastro"

5. Enviar as alterações ao GitHub

Depois de criar o commit, execute:

git push

Esse comando envia os commits para o repositório remoto.

«Importante: para enviar alterações diretamente, o colaborador precisa ter permissão de escrita no repositório e estar autenticado no GitHub.»

6. Receber alterações de outros colaboradores

Quando outra pessoa enviar atualizações, execute:

git pull

Assim, o projeto local receberá as alterações disponíveis no GitHub.

---

📖 Principais comandos do Git

Comando| Função
"git clone"| Baixa o projeto pela primeira vez
"git pull"| Recebe atualizações do GitHub
"git status"| Mostra o estado dos arquivos
"git add ."| Prepara as alterações
"git commit -m "mensagem""| Registra as alterações
"git push"| Envia os commits ao GitHub
"git log --oneline"| Mostra o histórico de commits

⚠️ Atenção ao trabalho em equipe

Para evitar problemas durante o desenvolvimento:

- Sempre execute "git pull" antes de começar a trabalhar.
- Faça commits com mensagens que expliquem as alterações.
- Evite que duas pessoas modifiquem simultaneamente as mesmas partes do código.
- Envie suas alterações com "git push" após criar o commit.
- Caso ocorra um conflito, resolva-o antes de continuar o envio.

Se duas pessoas alterarem a mesma parte de um arquivo, o Git poderá identificar um conflito. Nesse caso, será necessário comparar e organizar as alterações manualmente.

---

🗄️ Banco de dados

O sistema utiliza SQLite para armazenar os dados.

O banco de dados é criado automaticamente pela aplicação por meio do SQLAlchemy.

As tabelas são geradas a partir dos modelos existentes na pasta "models/".

«Atenção: o banco de dados local não é compartilhado automaticamente pelo GitHub. Cada instalação pode ter seu próprio arquivo de banco de dados. Não envie dados pessoais de alunos ao repositório.»

---

🔗 Repositório oficial

"Meu Desempenho — GitHub" (https://github.com/uCezar/Meu-Desempenho.git)

Projeto desenvolvido para acompanhamento do desempenho escolar.