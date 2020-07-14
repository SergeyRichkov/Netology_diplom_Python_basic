import requests
import pprint
token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
##params = {'user_ids': '4432126',
##          'fields': 'photo_id, verified, sex, bdate'
##          'city, country, home_town',
##          'v':'5.89',
##          'access_token': token
##          }

params = {'owner_id': '4432126',
          'album_id': 'profile',
          'extended' : 1,
          'photo_sizes': 1,
          'access_token': token,
          'v':'5.89'
          }

response = requests.get('https://api.vk.com/method/photos.get', params = params)
for number in range(response.json()['response']['count']):
    print(response.json()['response']['items'][number]['sizes'][-1]['url'])

