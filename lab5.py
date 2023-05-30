import requests


#Попытка аутентификации и получения куки
def authentication(login: str, password: str):
    auth = requests.post("https://ksu24.kspu.edu/api/v2/login/", data={
        'username': login,
        'password': password
    })

    if not auth.ok:
        print(f"Ошибка аутентификации. Код:{auth.status_code} {auth.text}")
        auth.raise_for_status()
    else:
        print(f"Аутентификация успешна. Статус код:{auth.status_code}")

    print("-" * 30)
    try:
        auth_cookie = auth.cookies.get_dict()["JWT"]
        return auth_cookie
    except():
        print("Ошибка получения куки аутентификации...")
        return


#Получение переменной по запросу с заданым ключем и фильтром
def get_value(url: str, auth_cookie, key, filter_by: dict = None):
    profile_request = requests.get(url=url, cookies={'JWT': auth_cookie})

    if profile_request.ok:
        data = profile_request.json()
        value = None
        if 'results' not in data.keys():
            if key in data.keys():
                value = data.get(key)
                return value
            else:
                print("Заданого ключа не существует...")
                return value
        else:
            if filter_by is None:
                for dictionary in data['results']:
                    if key in dictionary.keys():
                        value = dictionary.get(key)
                        return value
                    else:
                        print("Заданого ключа не обнаружено...")
                        return value
            else:
                filter_key = list(filter_by.keys())[0]
                for dictionary in data['results']:
                    if filter_key in dictionary.keys() and filter_by[filter_key] in dictionary[filter_key]:
                        if key in dictionary.keys():
                            value = dictionary.get(key)
                            return value
                        else:
                            print("Заданого ключа не обнаружено...")
                            return value
                print("Информации по заданому фильтру не обнаружено...")
                return value
    else:
        print(f"Запрос не выполнен. Кoд:{profile_request.status_code} - {profile_request.json()['detail']}")


#Вывод информации по данному запросу
def get_info(url, auth_cookie):
    profile_request = requests.get(url=url, cookies={'JWT': auth_cookie})

    if profile_request.ok:
        print("Запрос выполнен успешно...")

        data = profile_request.json()
        if "results" in data.keys():
            results_list = data["results"]
            for dictionary in results_list:
                for key in dictionary:
                    print(key, ": ", dictionary[key])
                print("-" * 30)
        else:
            for key in data:
                print(key, ": ", data[key])

        print("-" * 30)
    else:
        print(f"Запрос не выполнен. Кoд:{profile_request.status_code}")
        profile_request.raise_for_status()


def main():
    login = input("Логін: ")
    password = input("Пароль: ")

    auth_cookie = authentication(login=login, password=password)

    print("Запрос на получение информации о пользователе...")
    get_info(url="https://ksu24.kspu.edu/api/v2/my/profile/", auth_cookie=auth_cookie)

    print("Запрос на получение информации о студенте...")
    get_info(url="https://ksu24.kspu.edu/api/v2/my/students/", auth_cookie=auth_cookie)
    student_id = get_value(url="https://ksu24.kspu.edu/api/v2/my/students/", auth_cookie=auth_cookie, key="id")

    print("Запрос на получение информации о журнале студента...")
    get_info(url="https://ksu24.kspu.edu/api/v2/my/students/" + str(student_id) + "/recordbooks/", auth_cookie=auth_cookie)
    recordbook_id = get_value(url="https://ksu24.kspu.edu/api/v2/my/students/" + str(student_id) + "/recordbooks/",
                              auth_cookie=auth_cookie, key="id")

    print("Запрос на получение информации о дисциплинах")
    get_info(
        url="https://ksu24.kspu.edu/api/v2/my/students/" + student_id + "/recordbooks/" + recordbook_id + "/records",
        auth_cookie=auth_cookie)

    #print("Запрос на получении результата по дисциплине...")
    #descipline_result = get_value(
    #    url="https://ksu24.kspu.edu/api/v2/my/students/" + student_id + "/recordbooks/" + recordbook_id + "/records",
    #    auth_cookie=auth_cookie, key="result",
    #    filter_by={"discipline_name": "Моделювання бізнес-процесів"})
    #print(descipline_result)


main()
