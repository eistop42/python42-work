import requests

token = ''
base_url = f'https://api.telegram.org/bot{token}'

#отправляем запрос
res = requests.get(base_url+'/getMe')
# читаем ответ
print(res.text)

res = requests.get(base_url + '/getUpdates')
print(res.text)

user_id = 158448812

requests.get(base_url + '/sendMessage', params={'chat_id': user_id, 'text': 'привет'})
