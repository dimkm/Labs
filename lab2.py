# -*- coding: utf-8 -*-

def main():
    exp_var = ""
    exp_dictionary = {"1": "Привет ",
                      "2": "Мир",
                      "3": "!"}
    var_massive = [] # Пустий массив
    exp_cortage = (1,2,5,16,2,187) #кортеж


    #Выводим текст 'Привет Мир!' с помощью классов
    for key_values in exp_dictionary.values():
        #Як працюють змінні
        exp_var += key_values

    print(exp_var)
    print("_"*20)

    for i in range(20):
        var_massive.append(i) # Заповнюємо массив

    print(f"{var_massive}: - Массив до змін")

    var_massive.remove(1) # Видаляємо другий елемент в масиві
    print(f"{var_massive}: - Массив після видалення елемента")

    var_massive.append(40) # Додаємо число 40 до массиву
    print(f"{var_massive}: - Массив після додавання елемента\n")

    print("_"*20)

    print(f"{exp_cortage}: - Кортеж")
    print(f"{exp_cortage[1]}: - Виводимо другий елемент в кортежі")

if __name__ == '__main__':
    main()
