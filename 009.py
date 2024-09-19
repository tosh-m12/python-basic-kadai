import random

for i in range(1, 11):
    num = random.randint(1,20)
    print(f"{i}回目の結果は{num}です。")
    if num == 20:
        print("20が出たので繰り返し処理を強制終了します。")
        break

for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)