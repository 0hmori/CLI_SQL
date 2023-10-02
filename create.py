from db_config import User


def create_user():
    user_name = input("New user name > ")
    user_age = input("New user age > ")
    info1 = User(name=user_name, age=user_age)
    info1.save()
    print(f"Add new user: {user_name}")


if __name__ == "__main__":
    create_user()
