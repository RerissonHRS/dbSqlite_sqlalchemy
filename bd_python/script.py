import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#configurando a engine d BD
engine = create_engine('sqlite:///example.db', echo=True)

#Configurando a sessão
Session = sessionmaker(engine)

#Criando a tabela
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

def insert_usuario(nome_usuario, tipo_usuario):
    session = Session()
    try:
        if all ([nome_usuario, tipo_usuario]):
            usuario = Usuario(nome=nome_usuario, tipo=tipo_usuario)
            session.add(usuario)
            session.commit()
            print(f"Usuário {nome_usuario} adicionado com sucesso.")
        else:
            print("Nome e tipo são obrigatórios.")
    except Exception as e:
        session.rollback()
        print(f"Houve um erro ao adicionar usuário: {nome_usuario}. Erro: {e}")
    finally:
        session.close()

def select_usuarios(nome_usuario=''):
    session = Session()
    try:
        if nome_usuario:
            dados = session.query(Usuario).filter(Usuario.nome == nome_usuario)
        else:
            dados = session.query(Usuario).all()

        for i in dados:
            print(f"Usuário: {i.nome} - Tipo: {i.tipo}")

    except Exception as e:
        print(f"Houve um erro ao buscar usuários. Erro: {e}")
    finally:
        session.close()

def update_nome_usuario(id_usuario, nome_usuario):
    session = Session()
    try:
        if all([id_usuario, nome_usuario]):
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            usuario.nome = nome_usuario
            session.commit()
            print(f"Usuário com ID {id_usuario} atualizado para {nome_usuario}.")
        else:
            print(f"Usuário com ID {id} não encontrado. Obrigatório passar o ID.")
    except Exception as e:
        session.rollback()
        print(f"Houve um erro ao atualizar usuário: {e}")
    finally:
        session.close()

def delete_usuario(id_usuario):
    session = Session()
    try:
        if id_usuario:
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            session.delete(usuario)
            session.commit()
            print(f"Usuário com ID {id_usuario} deletado com sucesso.")
        else:
            print(f"Usuário com ID {id_usuario} não encontrado.")
    except Exception as e:
        session.rollback()
        print(f"Houve um erro ao deletar usuário: {e}")
    finally:
        session.close()   

if __name__ == "__main__":
    os.system('cls')  # Limpa o console
    Base.metadata.create_all(engine)  # Cria a tabela no banco de dados
    #insert_usuario("Alex", "Convidado")
    #select_usuarios("Rerisson")
    #update_nome_usuario(3, "Alex Milani")
    delete_usuario(3)
