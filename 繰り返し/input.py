while True:
    # 文字列を表示し、入力が入るまで待つ
    # breakされない限り入力をエンターしても再度入力待ち受けに入る
    word = input('Enter:')
    num = int(word)
    if num == 100:
        break
    print('next')