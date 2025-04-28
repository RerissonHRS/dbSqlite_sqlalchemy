# Gerenciador de Usuários com SQLite e SQLAlchemy

Este projeto é um simples sistema de CRUD (Create, Read, Update, Delete) de usuários usando Python, SQLite e SQLAlchemy como ORM.

## 🚀 Funcionalidades

- **Adicionar** usuários ao banco de dados
- **Buscar** todos os usuários ou por nome
- **Atualizar** o nome de um usuário pelo ID
- **Deletar** usuários pelo ID

## 🛠️ Tecnologias utilizadas

- Python 3.10+
- SQLite (via SQLAlchemy)
- SQLAlchemy ORM

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar
Editar
pip install sqlalchemy
Execute o script principal:

bash
Copiar
Editar
python seu_script.py

🧪 Como usar

# Exemplo: inserir um novo usuário
insert_usuario("Alex", "Administrador")

# Buscar todos os usuários
select_usuarios()

# Atualizar o nome do usuário com ID 3
update_nome_usuario(3, "Novo Nome")

# Deletar o usuário com ID 3
delete_usuario(3)
