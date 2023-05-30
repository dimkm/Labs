import datetime


class Person:
    name: str = None
    birthday: datetime.date = None

    def __init__(self, name: str, birthday: str):
        self.name = name
        self.birthday = datetime.datetime.fromisoformat(birthday).date()

    def __repr__(self):
        return f"{self.name} [{self.birthday}]"

    def __eq__(self, obj):
        return self.name == obj.name and self.birthday == obj.birthday


#Сортировка по именам
def sort_by_name(persons: list):
    persons.sort(key=lambda x: x.name)


#Сортировка по датам рождения
def sort_by_date(persons: list):
    persons.sort(key=lambda x: x.birthday)


#Сортировка по годам рождения
def sort_by_year(persons: list):
    persons.sort(key=lambda x: x.birthday.year)


#Сортировка по месяцам рождения
def sort_by_month(persons: list):
    persons.sort(key=lambda x: x.birthday.month)


#Сортировка по дням рождения
def sort_by_day(persons: list):
    persons.sort(key=lambda x: x.birthday.day)


#Сравнение двух списков
def equal(list_1: list, list_2: list):
    l1 = sorted(list_1, key=lambda x: x.name)
    l2 = sorted(list_2, key=lambda x: x.name)
    if l1 == l2:
        print(f"Списки одинаковые.")
        return True
    else:
        print(f"Списки разные.")
        return False


#Сравнение двух персон
def equal_two_person(pers_1: Person, pers_2: Person):
    if pers_1 == pers_2:
        print("Эти персоны одинаковы.")
        return True
    else:
        print(f"{pers_1.name} и {pers_2.name} разные.")
        return False


#Сравнение имен персон
def equal_name(pers_1: Person, pers_2: Person):
    if pers_1.name == pers_2.name:
        print("У этих персон одинаковые имена.")
        return True
    else:
        print(f"У {pers_1.name} и {pers_2.name} разные имена.")
        return False


#Сравнение полных дат рождения
def equal_birthday_date(pers_1: Person, pers_2: Person):
    if pers_1.birthday == pers_2.birthday:
        print(f"У {pers_1.name} и {pers_2.name} одинаковая дата рождения.")
        return True
    else:
        print(f"У {pers_1.name} и {pers_2.name} разные даты рождения.")
        return False


#Сравнение годов рождения
def equal_birthday_year(pers_1: Person, pers_2: Person):
    if pers_1.birthday.year == pers_2.birthday.year:
        print(f"У {pers_1.name} и {pers_2.name} одинаковый год рождения.")
        return True
    else:
        print(f"У {pers_1.name} и {pers_2.name} разные года рождения.")
        return False


#Сравнение месяцев рождения
def equal_birthday_month(pers_1: Person, pers_2: Person):
    if pers_1.birthday.month == pers_2.birthday.month:
        print(f"У {pers_1.name} и {pers_2.name} одинаковый месяц рождения.")
        return True
    else:
        print(f"У {pers_1.name} и {pers_2.name} разные месяца рождения.")
        return False


#Сравнение дней рождения
def equal_birthday_day(pers_1: Person, pers_2: Person):
    if pers_1.birthday.day == pers_2.birthday.day:
        print(f"У {pers_1.name} и {pers_2.name} одинаковый день рождения.")
        return True
    else:
        print(f"У {pers_1.name} и {pers_2.name} разные дни рождения.")
        return False


def main():
    p1 = Person(name="Isabela", birthday="2004-03-03")
    p2 = Person(name="Larissa", birthday="2004-04-03")

    persons_1 = [
        Person(name="Ivan", birthday="2000-01-02"),
        Person(name="Olga", birthday="1998-10-08"),
        Person(name="Ben", birthday="1999-02-03"),
        Person(name="Sam", birthday="2001-01-10"),
        Person(name="Lina", birthday="2001-12-09")
    ]
    persons_2 = [
        Person(name="Ben", birthday="1999-02-03"),
        Person(name="Ivan", birthday="2000-01-02"),
        Person(name="Sam", birthday="2001-01-10"),
        Person(name="Lina", birthday="2001-12-09"),
        Person(name="Olga", birthday="1998-10-08")
    ]

    print(f"Сравниваем два списка: \n{persons_1} \n{persons_2}")
    equal(persons_1, persons_2)

    print(f"\nСравниваем две персоны: {p1} и {p2}")
    equal_two_person(p1, p2)
    equal_name(p1, p2)

    equal_birthday_date(p1, p2)
    equal_birthday_year(p1, p2)
    equal_birthday_month(p1, p2)
    equal_birthday_day(p1, p2)

    print("\nСортировка списка персон:")

    print(f"До сортировки: {persons_1}")

    sort_by_year(persons_1)
    print(f"После сортировки по годам: {persons_1}")
    sort_by_name(persons_1)
    print(f"После сортировки по именам: {persons_1}")


main()
