class User:
    def __init__(self, user_id, user_name, user_gen):
        self.id = user_id
        self.name = user_name
        self.gender = user_gen


uid = input("Enter your id:")
uname = input("Enter your name:")
ugn = input("Enter your gender")

user_1 = User(uid, uname, ugn)

print(user_1.id)
print(user_1.name)
print(user_1.gender)
