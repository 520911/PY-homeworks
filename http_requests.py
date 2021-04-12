import requests

url = 'https://superheroapi.com/api/2619421814940190/search/'
names_of_characters = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]


def super_hero_func(hero_url, list_of_dicts):
    new_dict = {}
    for names in names_of_characters:
        main_url = url + names['name']
        response = requests.get(main_url)
        data = response.json()
        new_dict[names['name']] = int(
            data['results'][0]['powerstats']['intelligence'])  # Получение словарей имя: значение интеллекта

    for intel in sorted(new_dict.items(), key=lambda para: para[1], reverse=True):  # Сортировка по значениям словаря
        print(f'Самый умный супергерой: {intel[0]}, его интеллект равен: {intel[1]}')
        break  # Остановка после первого прохода т.к. это самое большое значение


super_hero_func(url, names_of_characters)
