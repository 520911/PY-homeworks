import requests

stack_url = 'https://api.stackexchange.com/2.2/questions?'
headers = {'Accept': 'application/json'}
params = {
    'fromdate': '1618099200',
    'todate': '1618272000',
    'order': 'asc',
    'sort': 'activity',
    'tagged': 'python',
    'site': 'stackoverflow'
}
response = requests.get(stack_url, headers=headers, params=params)
stack_dict = response.json()
print('Вывод последний вопросов по тегу python:')
print()
for items in stack_dict['items']:
    print(items['title'])
