from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Base para a definição das classes
Base = declarative_base()

# Definição da classe Cliente
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String, unique=True)

    # Relacionamento com a tabela Conta
    contas = relationship('Conta', back_populates='cliente')

# Definição da classe Conta
class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))

    # Relacionamento com a tabela Cliente
    cliente = relationship('Cliente', back_populates='contas')

# Configuração do SQLite
engine = create_engine('sqlite:///banco.db')
Base.metadata.create_all(engine)

# Criação da sessão
Session = sessionmaker(bind=engine)
session = Session()

# Inserção de dados de exemplo
cliente1 = Cliente(nome='João Silva', email='joao@exemplo.com')
cliente2 = Cliente(nome='Maria Oliveira', email='maria@exemplo.com')

conta1 = Conta(tipo='Corrente', saldo=1500, cliente=cliente1)
conta2 = Conta(tipo='Poupança', saldo=3000, cliente=cliente1)
conta3 = Conta(tipo='Corrente', saldo=2000, cliente=cliente2)

session.add(cliente1)
session.add(cliente2)
session.add(conta1)
session.add(conta2)
session.add(conta3)
session.commit()

# Recuperação de dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f"Cliente: {cliente.nome}, Email: {cliente.email}")
    for conta in cliente.contas:
        print(f"  Conta {conta.tipo}, Saldo: {conta.saldo}")

# Recuperação de um cliente específico
cliente_joao = session.query(Cliente).filter_by(nome='João Silva').first()
print(f"Cliente específico: {cliente_joao.nome}, Email: {cliente_joao.email}")
