from db_config import Info


def dispray_all_info():
    for usre_info in Info.select():
        print(f"Name: {usre_info.name} Age: {usre_info.age}")


#        print(usre_info.id, usre_info.name, usre_info.age)


if __name__ == "__main__":
    dispray_all_info()
