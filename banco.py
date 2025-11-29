import os
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from pprint import pprint

# CONFIGURAÇÃO
DB_NAME = "meu_banco"
COLLECTION_NAME = "livros"
DEFAULT_LOCAL_URI = "mongodb://localhost:27017"
MONGODB_URI = "mongodb+srv://kethelendamasceno235_db_user:Kl230498.@cluster0.nrwywkq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def get_client():
    """
    Tenta conectar usando MONGODB_URI (Atlas ou outro), se não, tenta local.
    """
    uri = os.environ.get("MONGODB_URI", DEFAULT_LOCAL_URI)
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    try:
        # força checagem de conexão
        client.admin.command('ping')
    except ServerSelectionTimeoutError as e:
        raise RuntimeError(f"Não foi possível conectar ao MongoDB em {uri}: {e}")
    return client

def get_db(client):
    return client[DB_NAME]

def list_collections(client):
    """Retorna lista de coleções (nomes) do banco."""
    db = get_db(client)
    return db.list_collection_names()

def get_collection(client, collection_name=COLLECTION_NAME):
    db = get_db(client)
    return db[collection_name]

# Funções CRUD simples
def inserir_livro(client, nome, caderno, preco, outros=None):
    """
    Insere um documento na coleção 'livros'.
    preco: número (float ou int)
    outros: dict com outros campos opcionais
    Retorna o inserted_id
    """
    col = get_collection(client)
    doc = {
        "nome": nome,
        "caderno": caderno,
        "preco": float(preco) if preco is not None else None
    }
    if outros:
        doc.update(outros)
    res = col.insert_one(doc)
    return res.inserted_id

def buscar_livros(client, filtro=None, limit=0):
    """Retorna cursor (lista) de documentos com filtro opcional."""
    col = get_collection(client)
    if filtro is None:
        filtro = {}
    cursor = col.find(filtro).limit(limit) if limit and limit > 0 else col.find(filtro)
    return list(cursor)

def atualizar_livro_por_id(client, _id, novos_campos):
    """Atualiza documento por _id (passe ObjectId ou string)."""
    from bson import ObjectId
    col = get_collection(client)
    filtro = {"_id": ObjectId(_id)} if not isinstance(_id, dict) else _id
    res = col.update_one(filtro, {"$set": novos_campos})
    return res.modified_count

def remover_livro_por_id(client, _id):
    from bson import ObjectId
    col = get_collection(client)
    filtro = {"_id": ObjectId(_id)} if not isinstance(_id, dict) else _id
    res = col.delete_one(filtro)
    return res.deleted_count

# Utilidade: imprimir colunas alinhadas (nome, caderno, preco)
def printar_livros_alinhado(livros):
    """
    Recebe uma lista de documentos (dicionários) e imprime as colunas:
    nome | caderno | preco
    tudo bem alinhado usando largura dinâmica.
    """
    # extrai valores seguros
    rows = []
    for d in livros:
        nome = str(d.get("nome", ""))[:60]  # limitar tamanho para visual
        caderno = str(d.get("caderno", ""))
        preco = d.get("preco", "")
        # formata preco como string com 2 casas se for numérico
        if isinstance(preco, (int, float)):
            preco = f"{preco:.2f}"
        else:
            preco = str(preco)
        rows.append((nome, caderno, preco))

    # calcula larguras
    w_nome = max([len(r[0]) for r in rows] + [len("NOME")])
    w_caderno = max([len(r[1]) for r in rows] + [len("CADERNO")])
    w_preco = max([len(r[2]) for r in rows] + [len("PRECO")])

    # cabeçalho
    header = f"{'NOME'.ljust(w_nome)}  {'CADERNO'.ljust(w_caderno)}  {'PRECO'.rjust(w_preco)}"
    sep = "-" * (w_nome + w_caderno + w_preco + 4)
    print(header)
    print(sep)
    for nome, caderno, preco in rows:
        print(f"{nome.ljust(w_nome)}  {caderno.ljust(w_caderno)}  {preco.rjust(w_preco)}")

# Exemplo de uso (quando executado como script)
if __name__ == "__main__":
    try:
        client = get_client()
    except RuntimeError as e:
        print("Erro de conexão:", e)
        raise SystemExit(1)

    print("Banco:", DB_NAME)
    print("Coleções existentes:", list_collections(client))

    # Inserir alguns documentos de exemplo (comente se não quiser inserir)
    exemplos = [
        ("Matemática Básica", "Caderno A", 29.9),
        ("História do Brasil", "Caderno B", 45.0),
        ("Arte Moderna", "Caderno C", 39.5),
    ]
    col = get_collection(client)
    # Só inserimos se a coleção estiver vazia (evita duplicar em execuções repetidas)
    if col.count_documents({}) == 0:
        print("Inserindo documentos de exemplo...")
        for nome, caderno, preco in exemplos:
            _id = inserir_livro(client, nome, caderno, preco)
            print(" inserido _id:", _id)

    # Buscar e imprimir alinhado
    livros = buscar_livros(client)
    print("\nLivros atuais:")
    printar_livros_alinhado(livros)

    # Exemplo de busca com filtro:
    print("\nLivros com preco > 30:")
    filtrado = buscar_livros(client, {"preco": {"$gt": 30}})
    printar_livros_alinhado(filtrado)

    # fechar conexão
    client.close()

