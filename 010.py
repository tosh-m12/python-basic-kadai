import random

# num = random.randint(0, 4)

# i = 1

# print(f"最初の値は{num}です。")

# while num != 0:
#     num = random.randint(0, 4)
    
#     if i == 5:
#         print("5回目なので繰り返し処理を強制終了します。")
#         break
    
#     print(f"現在の値は{num}です")
#     i = i + 1



sum = 0

while sum < 20:
    num = random.randint(1, 10)

    print(f"{num}が出ました。")
    if num % 2 == 0:
        print("偶数なので加算しません。")
        continue
    sum = sum + num
    print(f"現在の合計は{sum}です。")