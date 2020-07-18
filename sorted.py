# 辞書型の値でソートする
ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}
print(sorted(ranking))
# 値でソートする
print(sorted(ranking, key=ranking.get))

# 降順ソート
print(sorted(ranking, key=ranking.get, reverse=True))
