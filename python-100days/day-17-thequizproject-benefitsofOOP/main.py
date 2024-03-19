# class PascalCase:
#     pass

# user_1 = PascalCase()

#####

# class User:
#     pass

# user_1 = User()
# user_1.id = '001'
# user_1.username = 'sumit'

# print(user_1.username)

#####

class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User('001', 'sumit')
user_2 = User('002', 'salony')

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
