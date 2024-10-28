# To-Do App 📝

Olá, saudações!

Este projeto tem como finalidade explorar boas práticas de programação e consolidar conhecimentos na linguagem Python. Utilizamos FastAPI para criar uma API web, Pydantic para validação de dados, Alembic para gerenciamento de migrações de banco de dados e SQLite como sistema de banco de dados leve. O objetivo deste trabalho é desenvolver uma aplicação de gerenciamento de tarefas (To-Do) que permitirá aos usuários adicionar, listar, atualizar e remover tarefas. Ao final do projeto, será realizado o deploy da aplicação.

![Captura de tela de 2024-10-28 14-02-20](https://github.com/user-attachments/assets/3708308e-81b7-4b8a-bbff-2acc62ab04f5)


### 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte Implantação para saber como implantar o projeto.
### 📋 Pré-requisitos & 🔧 Instalação

Para instalar e executar este projeto, você precisará do Python instalado em sua máquina.

    Verifique se você possui o Python instalado:
        Você pode verificar a versão do Python com o seguinte comando:

    bash

python --version

Instale as dependências do projeto:

    No terminal, execute o seguinte comando:

bash

pip install -r requirements.txt

Configure o banco de dados:

    Execute as migrações usando Alembic:

bash

alembic upgrade head

Execute o servidor:

    Após a instalação e configuração, você pode iniciar o servidor FastAPI com o seguinte comando:

bash

    uvicorn main:app --reload

    Acesse a API:
        Abra seu navegador e acesse http://localhost:8000/docs para visualizar a documentação interativa da API.

### 🔩 Análise de Testes de Funcionalidade

yaml

Teste de Criação de Tarefa:

    Cenário:
        Um usuário cria uma nova tarefa através da API.
        O sistema armazena a tarefa no banco de dados.

Teste de Listagem de Tarefas:

    Cenário:
        Um usuário solicita a lista de tarefas existentes.
    Verificação:
        O sistema retorna todas as tarefas cadastradas.

Teste de Atualização de Tarefa:

    Cenário:
        Um usuário atualiza uma tarefa existente.
    Verificação:
        O sistema modifica a tarefa de acordo com os dados fornecidos.

Teste de Remoção de Tarefa:

    Cenário:
        Um usuário remove uma tarefa existente.
    Verificação:
        O sistema exclui a tarefa do banco de dados.

### 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

    Python - Linguagem de Programação
    FastAPI - Framework para Construção de APIs
    Pydantic - Validação de Dados
    Alembic - Migrações de Banco de Dados
    SQLite - Sistema de Banco de Dados Leve

### 🖇️ Colaborando

Por favor, leia o COLABORACAO.md para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

### 📌 Versão

(0.1.0) - 28-10-2024 (Elaboração Inicial da API) <br> (0.2.0) - 30-10-2024 (Implementação das Funcionalidades de Tarefas) <br> (0.3.0) - 02-11-2024 (Preparação para o Deploy)

### ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

    Pedro Henrique (EU) - Desenvolvedor da To-Do App

Você também pode ver a lista de todos os colaboradores que participaram deste projeto.

### 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo LICENSE.md para detalhes.

⌨️ com ❤️ por Pedrão Ribeiro 😊
