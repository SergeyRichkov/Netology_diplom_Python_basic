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

sizes_tuple = ('w', 'z', 'y', 'x', 'r', 'q', 'p', 'o', 'm', 's')


size_list_itog = []
like_list = []

for photo in items_list:
    like_list.append(photo['likes']['count'])    
    sizes_list_sorted = []
    number = items_list.index(photo)
    for i in sizes_tuple:
        for photo_type_dict in range(len(items_list[number]['sizes'])):
            if i in items_list[number]['sizes'][photo_type_dict]['type']:
                sizes_list_sorted.append(items_list[number]['sizes'][photo_type_dict])
    size_list_itog.append(sizes_list_sorted[0])
  
              
                


json_file = []
for photo1 in items_list:   
    how_many_likes = photo1['likes']['count']   
    photo_type = size_list_itog[items_list.index(photo1)]['type']
    load_date = time.gmtime(photo1['date'])
    if like_list.count(how_many_likes) > 1:
        json_file.append({'file_name' : f"{how_many_likes}" + '.jpeg' + f"__{time.strftime('%Hh%Mm %d%b %Y', load_date).replace(' ', '_')}", 'size' : photo_type})
    else:
        json_file.append({'file_name' : f"{how_many_likes}" + '.jpeg', 'size' : photo_type})

data1 = json_file
with open('json_file.json', 'w') as f:
    json.dump(data1, f, ensure_ascii=False, indent=2)
        

print(len(size_list_itog))

param = {'path': 'disk:/from_VK_photo', 'overwrite' : True }
header = {'Authorization':'AgAAAABC-feRAADLW4D33gzr_E7Uj9e3uLtiL24',}
create_folder = requests.put(
            'https://cloud-api.yandex.net:443/v1/disk/resources',
            params=param,
            headers=header)
print(create_folder.text)
    
for element in range(len(size_list_itog)):
    param1 = {'path': f"disk:/from_VK_photo/{json_file[element]['file_name']}",
              'url' : f"{size_list_itog[element]['url']}"}
   
    put_photo = requests.post(
            'https://cloud-api.yandex.net:443/v1/disk/resources/upload',
            params=param1,
            headers=header)
    
    print(put_photo.text)


    
    
    




     
            
