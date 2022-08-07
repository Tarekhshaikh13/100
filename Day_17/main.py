
class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Lavda")
user2 = User("002", "lassan")


user1.follow(user2)


print(user2.followers)
print(user2.following)


