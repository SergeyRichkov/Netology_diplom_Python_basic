import requests
import json
import time
from tqdm import tqdm

##token = 'AgAAAABC-feRAADLW4D33gzr_E7Uj9e3uLtiL24'

class YaUploader:

    def __init__(self, vk_id, token):
        self.vk_id = vk_id
        self.token = token
        
    def get_id(self):
        try:        
            params =
            {'user_ids': self.vk_id,
              'access_token': ('958eb5d439726565e9333aa30e50e0f937ee432e'
                      '927f0dbd541c541887d919a7c56f95c04217915c32008'),
              'v':'5.89'
              }
            response = requests.get('https://api.vk.com/method/users.get',
                                    params = params)
##            response.json()
            ID = response.json()['response'][0]['id']
        except KeyError:            
            ID = response.json()['error']['error_msg']     
        return ID

    def get_photo_information(self):
        try:
            params = {'owner_id': self.get_id(),
              'album_id': 'profile',
              'extended' : 1,
              'photo_sizes': 1,
              'access_token': ('958eb5d439726565e9333aa30e50e0f937ee432e927f'
                               '0dbd541c541887d919a7c56f95c04217915c32008'),
              'v':'5.89'
              }
            response = requests.get('https://api.vk.com/method/photos.get',
                                    params = params)
            items_list = response.json()['response']['items']

            sizes_tuple = ('w', 'z', 'y', 'x', 'r', 'q', 'p', 'o', 'm', 's')
            size_list_final = []
            like_list = []
            json_file = []

            
            for photo in items_list:
                like_list.append(photo['likes']['count'])    
                sizes_list_sorted = []
                number = items_list.index(photo)
                for i in sizes_tuple:
                    for photo_type_dict in range(
                        len(items_list[number]['sizes'])):
                        if i in (items_list[number]['sizes'][photo_type_dict]
                        ['type']):
                            (sizes_list_sorted.append(items_list[number]['sizes']
                            [photo_type_dict]))
                size_list_final.append(sizes_list_sorted[0])
                                      
        
            for photo1 in items_list:   
                how_many_likes = photo1['likes']['count']   
                photo_type = size_list_final[items_list.index(photo1)]['type']
                load_date = time.gmtime(photo1['date'])
                if like_list.count(how_many_likes) > 1:
                    json_file.append({'file_name': f"{how_many_likes}" + '.jpeg'
+ f"__{time.strftime('%Hh%Mm %d%b %Y', load_date).replace(' ', '_')}",
'size' : photo_type})
                else:
                    json_file.append({'file_name': f"{how_many_likes}" +
                                      '.jpeg', 'size' : photo_type})

            data1 = json_file
            with open('json_file.json', 'w') as f:
                json.dump(data1, f, ensure_ascii=False, indent=2)

            json_file.reverse()
            size_list_final.reverse()
            like_list.reverse()
                
            return  (json_file,size_list_final, like_list)
        except KeyError:
           return response.json()['error']
    

    def upload_to_ya_disk(self, how_many_photos = 2):
        if how_many_photos > len(self.get_photo_information()[0]):
            how_many_photos = len(self.get_photo_information()[0])          
            try:
                param = {'path': 'disk:/from_VK_photo',
                         'overwrite' : False}
                header = {'Authorization': self.token}
                create_folder = requests.put(
                        'https://cloud-api.yandex.net:443/v1/disk/resources',
                            params=param,
                            headers=header)
                    
                for element in tqdm(range(how_many_photos)):
                    param = {'path':
f"disk:/from_VK_photo/{self.get_photo_information()[0][element]['file_name']}",
                'url' : f"{self.get_photo_information()[1][element]['url']}"}
                   
                    put_photo = requests.post(
                            'https://'
                            'cloud-api.yandex.net:443/v1/disk/resources/upload',
                            params=param,
                            headers=header)
                    if str(put_photo) != '<Response [202]>':
                        if str(put_photo) == '<Response [401]>':
                            print('Не удалось авторизоваться.'
                                  'Проверьте корректность токена.')
                        else:
                            print(put_photo.json()['message'])
                        break
                time.sleep(1)
                return print('Фотографии успешно загружены!')
            except KeyError:
                if self.get_photo_information()['error_code'] == 30:
                    print('Профиль является приватным\n'
                    'Информация, запрашиваемая о профиле,'
                    'недоступна с используемым ключом доступа')
                elif self.get_photo_information()['error_code'] == 100:
                    print('Вероятно,'
                          'введен некорректный идентификатор пользователя.'
                          'Проверьте его правильность.')
                else:
                    print(self.get_photo_information()['error_msg'])
                return 
        
       
if __name__ == '__main__':
    ID = input('Введите идентификаторы пользователя или'
               'короткое имя(screen_name):\n')
    token = input('Введите токен пользователя Яндекс.Диск:\n')
    
    uploader = YaUploader(ID, token)
    result = uploader.upload_to_ya_disk(5)           
