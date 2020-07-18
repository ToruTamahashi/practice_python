"""
{
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}
"""

import json
# dict型で同様に記述可能

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

print(j)
print("#################3")
# dict -> json形式に変換
print(json.dumps(j))


# json -> dict形式に変換
a = json.dumps(j)
json.loads(a)

# 書き込み
with open('test.json', 'w') as f:
    json.dump(j, f)

# 読み込み
with open('test.json', 'r') as f:
    json.load(j, f)

#