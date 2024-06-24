class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        if access_level in ['user', 'admin']:
            self.__access_level = access_level

    def __str__(self):
        return f"Пользователь(ID: {self.__user_id}, Имя: {self.__name}, Уровень доступа: {self.__access_level})"


# Пример использования
user1 = User(1, "Алена")
print(user1)


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.set_access_level('admin')

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} Добавил  администратор {self.get_name()}.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь ID {user_id} Удалил администратор {self.get_name()}.")
                return
        print(f"User ID {user_id} not found.")


# Пример использования
admin1 = Admin(2, "Борис")
print(admin1)

# Создаем список пользователей
users = []

# Создаем пользователей
user1 = User(1, "Алена")
user2 = User(2, "Сергей")
user3 = User(3, "Мария")

# Создаем администратора
admin1 = Admin(0, "Борис")

# Добавление пользователей администратором
admin1.add_user(users, user1)
admin1.add_user(users, user2)
admin1.add_user(users, user3)

# Проверка списка пользователей
for user in users:
    print(user)

# Удаление пользователя администратором
admin1.remove_user(users, 2)

# Проверка списка пользователей после удаления
for user in users:
    print(user)







