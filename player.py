class Player:
    def __init__(self, name="Незнакомец", hp=100):
        self.name = name  # Имя игрока (по умолчанию Незнакомец)
        self.hp = int(hp)  # здоровье игрока
        self.inventory = []  # инвентарь, где хранятся предметы

    def add_item(self, item):  # добавление предмета в инвентарь
        self.inventory.append(item)

    def remove_item(self, item):  # удаляет предмет из инвентаря, возвращает True если предмет был, иначе False
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        else:
            return False

    def show_inventory(self):  # выводит инвентарь в консоль
        if self.inventory:
            for i, item in enumerate(self.inventory, 1):
                print(f"   {i}. {item}")
        else:
            print('Пусто')
        print()

    def has_item(self, item):  # проверяет наличие предмета в инвентаре
        return item in self.inventory

    def receive_damage(self, damage):  # нанесение урона игроку, здоровье не может стать меньше 0
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def die(self):  # возвращает True если игрок мёртв (здоровье <= 0)
        if self.hp <= 0:
            return True
        else:
            return False

    def use_syringe(self):  # шприц: восстанавливает 10 HP, но не выше 100. Возвращает True если шприц был
        if self.has_item("Шприц"):
            self.remove_item("Шприц")
            self.hp += 10
            if self.hp > 100:
                self.hp = 100
            print("╔════════════════════════════════════════════════════════════════════════╗")
            print(f"║ Вы использовали шприц. HP: {self.hp}/100                               ║")
            print("╚════════════════════════════════════════════════════════════════════════╝")
            return True
        else:
            print("╔════════════════════════════════════════════════════════════════════════╗")
            print("║  У вас нет шприцев!                                                    ║")
            print("╚════════════════════════════════════════════════════════════════════════╝")
            return False  # если шприца не было, возвращает False

    def save_data(self):  # сохраняет данные игрока
        inventory_str = ",".join(self.inventory)
        return f"{self.name}|{self.hp}|{inventory_str}"

    def load_data(self, data):  # загружает данные игрока
        parts = data.split("|")  # разбиваем строку
        if len(parts) >= 2:
            self.name = parts[0]
            try:  # пробуем преобразовать здоровье в число, если ошибка - оставляем 100
                self.hp = int(parts[1])
            except:
                self.hp = 100
            if len(parts) >= 3 and parts[2]:  # если есть третья часть и она не пустая - разбиваем её по запятым в список
                self.inventory = parts[2].split(",")
            else:
                self.inventory = []