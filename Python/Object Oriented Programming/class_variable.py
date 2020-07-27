class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    @classmethod
    def number_of_users(cls):
        print(f"총 유저 수는: {cls.count}입니다")

    @staticmethod
    def is_valid_email(email_address):
        return "@" in email_address

user1 = User("김보현", "bulias@naver.com", "12345")

print(User.count)
print(user1.name)

print(user1.is_valid_email(user1.email))