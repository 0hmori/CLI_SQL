from db_config import Info


def prints():
    print("===== Welcome to CRM Application =====")
    print("[S]how: Show all users info")
    print("[A]dd: Add new user")
    print("[Q]uit: Quit The Application")
    print("======================================")
    print()


def dispray_all_info():
    for usre_info in Info.select():
        print(f"Name: {usre_info.name} Age: {usre_info.age}")


def create_user():
    user_name = input("New user name > ")
    user_age = input("New user age > ")
    info = Info(name=user_name, age=user_age)
    info.save()
    print(f"Add new user: {user_name}")


prints()


def main():
    command = ""

    while True:
        # for usre_info in Info.select():
        # print(f"Name: {usre_info.name} Age: {usre_info.age}")

        command = input("Your command > ")

        if command == "S":
            dispray_all_info()
            print()

        elif command == "A":
            create_user()
            print()

        elif command == "Q":
            print("Bye!")
            break

        else:
            print(f"{command}: command not found")
            print()


if __name__ == "__main__":
    main()
