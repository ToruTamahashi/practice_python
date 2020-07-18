import dbm

# dbmはint型が入らない

# データ書き込み
with dbm.open('cache','c') as db:
    db['key1'] = 'value1'
    db['key2'] = 'value2'

# データ読み込み
with dbm.open('cache','r') as db:
    print(db.get('key1'))