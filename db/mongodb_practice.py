"""
実行する前に
docker run -p 27017:27017 --name dev-mongo -d mongo
でmongodbのコンテナを起動しておく
docker rm -f [コンテナID]
でコンテナを削除
"""
# あまり検索を多用しない場合
# ログをとったりするときに使うことが多い（datetimeで検索をかける）
import datetime

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

# mongodbをあらゆる形式(上からstr,json,dict,date)を値に設定できる
stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.utcnow()
}

stack2 = {
    'name': 'customer2',
    'pip': ['java', 'go'],
    'info': {'os': 'windows'},
    'data': datetime.datetime.utcnow()
}

db_stacks = db.stacks
# stack1をインサートしてから、idを返す
stack_id = db_stacks.insert_one(stack1).inserted_id
# stackidとデータ型表示
print(stack_id, type(stack_id))
print('#####')

# 指定したstack_idと連携しているデータを検索
#print(db_stacks.find_one({'_id': stack_id}))
# 別の方法で検索(同じ結果になる)
#print(db_stacks.find_one({'name': 'customer1'}))

# stack2をインサート
stack_id = db_stacks.insert_one(stack2).inserted_id

# ループですべてのスタックを表示
for stack in db_stacks.find():
    print(stack)
print('####################3')
# 現在時刻より過去のスタックを一覧表示
now = datetime.datetime.utcnow()
for stack in db_stacks.find({'data': {'$lt': now}}):
    print(stack)

print('YYYYYYYYYYYYYYYYYYY')
# スタックをアップデートする
db_stacks.find_one_and_update(
    {'name': 'customer1'}, {'$set': {'name': 'YYY'}}
)
print(db_stacks.find_one({'name': 'YYY'}))


# スタックをデリートする
db_stacks.delete_one({'name': 'YYY'})