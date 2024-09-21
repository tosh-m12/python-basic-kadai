
members_data = {"侍太郎": 30, "侍一郎": 25, "侍二郎": 21, "侍三郎": 19, "侍四郎": 16}

class Human:
    def __init__(self):
        self.name = ""
        self.age = ""
    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}さんは大人です")
        else:
            print(f"{self.name}さんは大人ではありません")

members_list = []

for key, value in members_data.items():
    member = Human()
    member.name = key
    member.age = value
    members_list.append(member)

for human in members_list:
    print(human.name, human.age)
    human.check_adult()