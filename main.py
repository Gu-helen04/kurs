import time
from tqdm import tqdm
import requests
from pprint import pprint
from yadisk import YaDisk
from progress.bar import IncrementalBar

def import_yandex (url_list):
    response = YaDisk(ya_token)
    for name, url_ in url_list.items():
        flag = response.upload_file_(url_, '/vk/' + str(name))
        if flag == False:
            print(f'ОЙ...Что то пошло не так...\nОШИБКА загрзки {name}: {url_}')
            break

if __name__ == '__main__':
    hosts = 'https://cloud-api.yandex.net'
    URL = 'https://api.vk.com/method/photos.get'
    ya_token = ''
    token = 'a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd'
    params = {
        'owner_id': '552934290',
        'album_id': 'profile',
        'photo_sizes': '1',
        'access_token': token,
        'extended': '1',
        'v': '5.131'
    }
    request_vk = requests.get(URL, params=params)
    pprint(request_vk.json())
    items_teg = (request_vk.json())['response']
    all_photo = items_teg['items']
    url_list_ = {}
    url_list = []

    for all_size_one_photo in all_photo:
        list_size_one_photo = all_size_one_photo['sizes']
        number_elements_list = len(list_size_one_photo)
        likes_photo = all_size_one_photo['likes']
        name_like = likes_photo['count']
        if url_list_.get(name_like) == None:
            url_list_[name_like] = list_size_one_photo[number_elements_list - 1]['url']
        else:
            url_list_[str(name_like)+'_'] = list_size_one_photo[number_elements_list - 1]['url']
        url_list.append(url_list_)
        url_list_ = {}
    print('\n')
    for i in tqdm(url_list):
        import_yandex(i)
        time.sleep(1)





    # res = YaDisk(ya_token)
    # for i in url_list:
    #     res.upload_file_(i,'/test/+')
    # zag = YaDisk(ya_token)
    # check = 0
    # for i in url:
    #     check += 1
    #     # zag.get_files_list(i,str(check))
    #     url_ = f'{self.hosts}/v1/disk/resources/files/
    #     req = requests.post(i,)



