from pymongo import MongoClient

# Conexão com o MongoDB Atlas
client = MongoClient('mongodb+srv://<usuario>:<senha>@<cluster-url>/<nome-do-banco>?retryWrites=true&w=majority')
db = client['nome_do_banco']
colecao = db['bank']

# Inserção de documentos
clientes = [
    {
        "nome": "João Silva",
        "email": "joao@exemplo.com",
        "contas": [
            {"tipo": "Corrente", "saldo": 1500},
            {"tipo": "Poupança", "saldo": 3000}
        ]
    },
    {
        "nome": "Maria Oliveira",
        "email": "maria@exemplo.com",
        "contas": [
            {"tipo": "Corrente", "saldo": 2000}
        ]
    }
]

colecao.insert_many(clientes)

# Recuperação de todos os documentos
for cliente in colecao.find():
    print(cliente)

# Recuperação de um cliente específico pelo nome
cliente_joao = colecao.find_one({"nome": "João Silva"})
print(cliente_joao)

# Recuperação de clientes com saldo em conta corrente maior que 1000
clientes_saldo = colecao.find({"contas": {"$elemMatch": {"tipo": "Corrente", "saldo": {"$gt": 1000}}}})
for cliente in clientes_saldo:
    print(cliente)
