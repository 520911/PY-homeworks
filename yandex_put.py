from pprint import pprint

import requests
import os

ya_token = ''
file_path = os.path.abspath('C:/testfolder/testfile.txt')


def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(ya_token)
    }


def get_files():
    ya_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    headers = get_headers()
    response = requests.get(ya_url, headers=headers)
    print(response)
    return response.json()


def get_upload_link(disk_file_path):
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    headers = get_headers()
    params = {"path": disk_file_path, "overwrite": "true"}
    response = requests.get(upload_url, headers=headers, params=params)
    pprint(response.json())
    return response.json()


def upload_file_to_disk(disk_file_path, filename):
    href = get_upload_link(disk_file_path=disk_file_path).get("href", "")
    response = requests.put(href, data=open(filename, 'rb'))
    response.raise_for_status()
    if response.status_code == 201:
        print("Success")


get_headers()
pprint(get_files())
get_upload_link('test')
upload_file_to_disk('testfile.txt', file_path)
