Meu Desempenho

Sistema web para acompanhamento do desempenho escolar dos alunos, desenvolvido com Python, Flask, SQLite, HTML, CSS e JavaScript.

1. Sobre o projeto

O Meu Desempenho é uma plataforma que permite aos alunos registrar e acompanhar suas notas escolares.

O sistema tem como objetivo facilitar a visualização do desempenho durante os quatro bimestres, permitindo que o estudante acompanhe suas médias e sua evolução ao longo do ano letivo.

Funcionalidades

- Cadastro e login de alunos.
- Cadastro de disciplinas.
- Registro de notas de provas e atividades.
- Organização das avaliações por disciplina e bimestre.
- Edição e exclusão de avaliações.
- Cálculo automático das médias.
- Acompanhamento da meta anual de 24 pontos.
- Visualização do desempenho escolar.

2. Tecnologias utilizadas

- Python: linguagem principal do sistema.
- Flask: framework utilizado para desenvolver a aplicação web.
- Flask-SQLAlchemy: integração com o banco de dados.
- SQLite: banco de dados utilizado para armazenar as informações.
- HTML: estrutura das páginas.
- CSS: estilização e aparência do sistema.
- JavaScript: funcionalidades e interações das páginas.
- Git e GitHub: controle de versões e colaboração.

3. Como baixar o projeto

Para obter os arquivos do projeto, é necessário ter o Git instalado.

Abra o terminal e execute:

git clone https://github.com/uCezar/Meu-Desempenho.git

Depois, entre na pasta:

cd Meu-Desempenho

4. Instalação das dependências

O projeto utiliza bibliotecas Python que precisam ser instaladas antes da execução.

Verifique se o Python está instalado:

python --version

Instale as dependências:

pip install -r requirements.txt

5. Configuração e execução

Depois de instalar as dependências, execute:

python app.py

O Flask iniciará o servidor local.

Abra o navegador e acesse:

http://127.0.0.1:5000

Observação: o banco de dados SQLite é criado automaticamente pela aplicação quando ela é iniciada, utilizando a configuração do projeto.

6. Primeiro acesso

Para participar do desenvolvimento, a pessoa precisa:

1. Ter uma conta no GitHub.
2. Receber um convite de colaboração do responsável pelo repositório.
3. Aceitar o convite.

O responsável pelo projeto pode enviar o convite acessando:

GitHub → Repositório → Settings → Collaborators → Add people.

Depois de aceitar o convite, o colaborador poderá enviar alterações diretamente ao repositório, conforme as permissões concedidas.

6.1. Baixar o projeto pela primeira vez

No computador do colaborador, é necessário instalar o Git e executar:

git clone https://github.com/uCezar/Meu-Desempenho.git

Depois:

cd Meu-Desempenho

O comando "git clone" baixa todos os arquivos e configura a conexão com o repositório remoto.

6.2. Configurar o Git

Cada colaborador deve configurar seu nome e e-mail uma única vez por instalação do Git:

git config --global user.name "Seu Nome"

git config --global user.email "seuemail@exemplo.com"

Essas informações identificam quem realizou cada commit.

6.3. Atualizar o projeto antes de trabalhar

Antes de começar a fazer alterações, execute:

git pull

Esse comando busca e integra as atualizações disponíveis no GitHub.

6.4. Registrar as alterações

Depois de modificar ou criar arquivos, execute:

git add .

Esse comando prepara as alterações para serem registradas.

Em seguida:

git commit -m "Descrição das alterações"

O commit registra as alterações no histórico do projeto.

Exemplo:

git commit -m "Adicionando tela de cadastro"

6.5. Enviar as alterações ao GitHub

Depois de criar o commit, execute:

git push

Esse comando envia os commits para o repositório remoto.

Importante: para enviar alterações diretamente, o colaborador precisa ter permissão de escrita no repositório e estar autenticado no GitHub.

6.6. Receber alterações de outros colaboradores

Quando outra pessoa enviar atualizações, basta executar:

git pull

Assim, o projeto local recebe as alterações disponíveis no GitHub.

7. Principais comandos do Git

Comando| Função
"git clone"| Baixa o projeto pela primeira vez.
"git pull"| Recebe atualizações do GitHub.
"git status"| Mostra o estado dos arquivos.
"git add ."| Prepara as alterações.
"git commit -m "mensagem""| Registra as alterações.
"git push"| Envia alterações ao GitHub.
"git log --oneline"| Mostra o histórico de commits.

8. Atenção ao trabalho em equipe

Para evitar problemas durante o desenvolvimento:

- Sempre execute "git pull" antes de começar a trabalhar.
- Faça commits com mensagens que expliquem as alterações.
- Evite que duas pessoas modifiquem simultaneamente as mesmas partes do código.
- Envie suas alterações com "git push" após criar o commit.
- Caso ocorra um conflito, resolva-o antes de continuar o envio.

Se duas pessoas alterarem a mesma parte de um arquivo, o Git poderá identificar um conflito. Nesse caso, será necessário comparar e organizar as alterações manualmente.

9. Banco de dados

O sistema utiliza SQLite para armazenar os dados.

O banco de dados é criado automaticamente pela aplicação por meio do SQLAlchemy.

As tabelas são geradas a partir dos modelos existentes na pasta "models/".

Atenção: o banco de dados local não é compartilhado automaticamente pelo GitHub. Cada instalação pode ter seu próprio arquivo de banco de dados. Não envie dados pessoais de alunos ao repositório.

---

Repositório oficial

GitHub: https://github.com/uCezar/Meu-Desempenho.git

Projeto Meu Desempenho — Acompanhamento do desempenho escolar.