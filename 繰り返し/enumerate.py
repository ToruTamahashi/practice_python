# 配列をforで回すときにインデックスを取得して表示したいとき
# 手間がかかる例
i = 0
for fruit in ['apple','banana','orange']:
    print(i, fruit)
    i += 1

# 配列をenumerate関数でくくることで第一引数に各配列のインデックスが格納される
for i, fruit in enumerate(['apple','banana','orange']):
    print(i, fruit)