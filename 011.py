# user_names = ["侍太郎", "侍一郎", "侍二郎", "侍三郎", "侍四郎"]

# for user_name in user_names:
#     print(user_name)


# personal_data = {"name": "侍太郎", "age": 36, "gender": "男性"}

# for value in personal_data.keys():
#     print(value)

# for a, b in personal_data.items():
#     print(f"{a}は{b}です。")


# user_names = ["侍太郎", "侍一郎", "侍二郎", "侍三郎", "侍四郎"]

# for index, value in enumerate(user_names):
#     print(f"{index} : {value}")

# user_names = ["侍太郎", "侍一郎", "侍二郎", "侍三郎", "侍四郎"]

# target = "侍二郎"

# for user_name in user_names:
#     print(user_name)

#     if (user_name == target):
#         print(f"{target}さんが見つかったので、繰り返し処理を強制終了します。")
#         break

score = {
    "国語": 80,
    "数学": 55,
    "理科": 70,
    "社会": 85,
    "英語": 60
}

print("合格した科目は以下の遠りです。")

for key, value in score.items():
    if (value < 70):
        continue
    print(f"{key} : {value}点")
