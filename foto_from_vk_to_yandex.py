import requests
import json
import time
##token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
##
##
##params = {'owner_id': '4432126',
##          'album_id': 'profile',
##          'extended' : 1,
##          'photo_sizes': 1,
##          'access_token': token,
##          'v':'5.89'
##          }
##
##response = requests.get('https://api.vk.com/method/photos.get', params = params)
##data = response.json()

##with open('response.txt', 'w') as f:
##    json.dump(data, f, ensure_ascii=False, indent=2)


with open('response.txt', encoding='utf8') as f:
    response_json = json.load(f)

items_list = response_json['response']['items']

sizes_tuple = ('w', 'z', 'y', 'x', 'r', 'q', 'p', 'm', 'o', 's')


size_list_itog = []
for photo in items_list:
    sizes_list_sorted = []
    number = items_list.index(photo)
    for i in sizes_tuple:
        for photo_type_dict in range(len(items_list[number]['sizes'])):
            if i in items_list[number]['sizes'][photo_type_dict]['type']:
                sizes_list_sorted.append(items_list[number]['sizes'][photo_type_dict])
    size_list_itog.append(sizes_list_sorted[0])


                
                
            

like_list = []

json_file = []
for photo1 in items_list:
    
    how_many_likes = photo1['likes']['count']   
    photo_type = size_list_itog[items_list.index(photo1)]['type']
    load_date = photo1['date']
    like_list.append(how_many_likes)
    if like_list.count(how_many_likes) > 1:
        json_file.append({'file_name' : f'{how_many_likes}' + '.jpeg' + f'/{time.ctime(load_date)}', 'size' : photo_type})
    else:
        json_file.append({'file_name' : f'{how_many_likes}' + '.jpeg', 'size' : photo_type})
print(json_file)
        
    
    
    

    
    
    




     
            
