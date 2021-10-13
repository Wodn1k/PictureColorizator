import requests
import json
import webbrowser

print('App for colorize photo')
#api_key = input('Введи свой Api Key: ')
api_key = '519ac6cf-504d-451e-85ca-a3b46b184431'
stat = 'да'

while stat == 'да':
    answer = input('Виберите вариант местоположения фото:\n1 - Фото находиться на компьютере.\n2 - Фото из интернета.\n')

    if answer == '1':
        path = input('Введи путь до своего фото: ')
        r = requests.post(
            "https://api.deepai.org/api/colorizer",
            files={
                'image': open(path, 'rb'),
            },
            headers={'api-key': api_key}
        )
        jsonData = r.text
        dictData = json.loads(jsonData)
        print("Ссылка на ваше обработаное фото : ", dictData['output_url'])
        webbrowser.open_new(dictData['output_url'])
        stat = input('Продолжить работу? да/нет \n')

    elif answer == '2':
        path = input('Вставте ссылку на своё фото: ')
        r = requests.post(
            "https://api.deepai.org/api/colorizer",
            data={
                'image': path,
            },
            headers={'api-key': api_key}
        )
        jsonData = r.text
        dictData = json.loads(jsonData)
        print("Ссылка на ваше обработаное фото : ", dictData['output_url'])
        webbrowser.open_new(dictData['output_url'])
        stat = input('Продолжить работу? да/нет \n')

    else:
        print('Неправильный ответ!')