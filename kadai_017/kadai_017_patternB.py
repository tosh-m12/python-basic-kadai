
members_data = {"侍太郎": 30, "侍一郎": 25, "侍二郎": 21, "侍三郎": 19, "侍四郎": 16}

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}さんは大人です")
        else:
            print(f"{self.name}さんは大人ではありません")

members_list = []

for name, age in members_data.items():
    human = Human(name, age)
    members_list.append(human)

for human in members_list:
    print(human.name, human.age)
    human.check_adult()