from pprint import pprint
import requests
import json

namesearch_url = "https://superheroapi.com/api/2619421814940190/search/"
superheroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]

for hero in superheroes:
    hero_r = requests.get(namesearch_url + hero['name'])
    hero['intelligence'] = int(hero_r.json()['results'][0]['powerstats']['intelligence'])
print(sorted(superheroes, key=lambda hero: -hero['intelligence'])[0]['name'])



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        api_base_url = 'https://cloud-api.yandex.net/'
        TOKEN = 'xxxxx'
        headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {TOKEN}'
        }
        get_url = requests.get(api_base_url + 'v1/disk/resources/upload', params={'path': 'Python_work/photo.jpg'},
                               headers=headers)

        upload_url = get_url.json()['href']
        aa = requests.put(upload_url, headers=headers, files={'f': open(file_path, 'rb')})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'C:\git\work\matrix.jpg'
    token = 'xxxxx'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)