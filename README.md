# Projeto Django - Biblioteca de Livros

Este projeto é um sistema de **biblioteca de livros** desenvolvido em Django. O objetivo é gerenciar livros, autores e usuários de forma simples e interativa, tornando o site mais dinâmico e facilitando a navegação entre as funcionalidades.

---

## 1. Configuração do Banco de Dados

Após clonar o repositório e instalar as dependências, é necessário criar o banco de dados da aplicação.

Execute os seguintes comandos no terminal:

```
python manage.py makemigrations
python manage.py migrate
```

- `makemigrations`: cria os arquivos de migração com base nos modelos definidos.  
- `migrate`: aplica as migrações e cria as tabelas do banco de dados.

---

## 2. Criação do Superusuário

Para acessar o painel administrativo do Django, é preciso criar um superusuário.  

Execute o comando:

```
python manage.py createsuperuser
```

Informe um nome de usuário, e-mail (opcional) e senha.

---

## 3. Acesso ao Painel Administrativo

Após iniciar o servidor com:

```
python manage.py runserver
```

Você pode acessar o painel administrativo em:

```
http://127.0.0.1:8000/admin/
```
No projeto, também foi implementado um **botão de acesso direto ao painel admin** na interface web. Esse botão redireciona o superusuário para o painel administrativo com apenas um clique.

Essa funcionalidade foi adicionada **para deixar o site mais dinâmico e proporcionar uma melhor interação com as funcionalidades administrativas**, facilitando o gerenciamento do conteúdo diretamente a partir da página principal.

---

## 4. Populando o Banco de Dados

Após acessar o painel administrativo com o superusuário, é possível **popular o banco de dados** cadastrando livros, autores e editoras diretamente pelo painel.  

Esses dados passam a ser exibidos automaticamente nas páginas do site, refletindo as atualizações em tempo real.

---

## 5. Objetivo do Projeto

O propósito deste projeto foi integrar a administração do Django de forma mais fluida à experiência de navegação do site, permitindo um gerenciamento ágil dos dados e um contato mais intuitivo entre o usuário e o sistema da biblioteca.
