# neo4j-python-driverをインストール
from neo4j import GraphDatabase


driver = GraphDatabase.driver(
    'bolt://localhost:7687',
    auth=('neo4j','pass'),
    encrypted=False
)
# tx:transactionのこと
# 処理内容を定義
def clear_db(tx):
    tx.run('MATCH (n) DETACH DELETE n')
def add_friend(tx, name, friend_name=None):
    if not friend_name:
        return tx.run('CREATE (p:Person {name: $name}) RETURN p', name=name)
    return tx.run('MATCH (p:Person {name: $name})'
                  'CREATE (p)-[:FRIEND]->(:Person {name: $friend_name})',
                  name=name, friend_name=friend_name)
def add_Jun(tx):
    tx.run('CREATE(jun:Person {name:"Jun"})'
           'RETURN jun')

def print_frinend(tx, name):
    for record in tx.run('MATCH (p {name: $name})-[FRIEND]->(yourFriends)'
                         'RETURN p.yourFriends', name=name):
        print(record)
# ここから処理させたい関数を呼び出す
with driver.session() as session:
    session.write_transaction(clear_db)
    session.write_transaction(add_Jun)
"""
    session.write_transaction(add_friend, 'Jun')
    for f in ['Mike', 'Nancy']:
        session.write_transaction(add_friend, 'Jun', f)
    session.read_transaction(print_frinend, 'jun')
"""