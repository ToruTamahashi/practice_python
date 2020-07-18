l = [1,2,5]
i = 5


try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
else:
    # tryが正常に実行されたときにここに入る
    print('done')
finally:
    # 必ず最後はここが実行される
    print('clean up')
print('last')