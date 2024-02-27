Olá!

Este é o meu teste técnico para a vaga de Desenvolvedor Full Stack Jr. na PAM.

Trata-se de um sistema simples de contas e notas, onde o professor pode cadastras as notas dos alunos e o aluno pode ver as suas notas, além de faltas.

O projeto foi feito utilizando Django, Django RestFramework, Django ORM e Jsonwebtoken.

O projeto possui sistema de autenticação e rotas protegidas, sendo necessário passar o token de acesso gerado pelo jsonwebtoken, além de retornar no token informações como o id do usuário e se ele é ou não um professor, garantindo que um aluno não possa acessar a página e rotas dos professores.

Para rodar o projeto:

Garanta que tenha instalado no seu computador:

Python
pip
PostgresSQL

Comece criando um abiente virtual em python, acesse seu terminal GitBash e digite:

python -m venv venv

Depois é necessário acessar o ambiente virtual, no mesmo terminal digite:

source venv/Scripts/activate

Após isso vamos instalar as dependencias para que o projeto possa funcionar corretamente, esse repositório já possui o arquivo requirements.txt, contendo todas as dependencias.
Com o ambiente virtual ativo, digite no terminal:

pip install -r requirements.txt

Após isso, é necessário criar um banco de dados PostgreSQL localmente, para isso vou deixar um tutorial para que você consiga realizar:

https://halleyoliv.gitlab.io/pgdocptbr/sql-createdatabase.html

Lembre-se de anotar: Nome de usuário, senha, nome do banco.

Com esses dados em mãos, vá ate:

ProjetoEscola/settings.py

Procure pela seção DATABASES e preencha com as informações
"NAME" coloque o nome do banco
"USER" coloque o nome de usuario
"PASSWORD" coloque a senha do usuario Postgres

e garanta que a sua configuração de host e portas são as mesmas já definidas no projeto.

Com tudo certo, podemos rodar as migrations para realizar a criação das tabelas automaticamente em nosso banco de dados.
No mesmo terminal digite:

python manage.py migrate

Após isso, estará tudo pronto para rodarmos o servidor localmente, digite no terminal:

python manage.py runserver