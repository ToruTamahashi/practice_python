count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        # ループを強制的に抜ける
        break
    if count == 2:
        count += 1
        # 以降の処理を飛ばして次のループに入る
        continue
    print(count)
    count += 1

    