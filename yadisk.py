from pprint import pprint
import requests
import time

class YaDisk:
    hosts = 'https://cloud-api.yandex.net'
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload_file_g(self, id_operation):
        url = f'{self.hosts}/v1/disk/operations/'+id_operation
        headers = self.get_headers()
        res = requests.get(url, headers=headers)
        if res.json()['status'] == 'success':
            return True
        else:
            return False

    def upload_file_(self, url_, file_name):
        url = f'{self.hosts}/v1/disk/resources/upload/'
        params = {'path': file_name, 'url': url_}
        headers = self.get_headers()
        res = requests.post(url, params=params, headers=headers, )
        id_operation = str(res.json().get('href')).partition('operations/')[2]
        time.sleep(3)
        boot_switch = self.upload_file_g(id_operation)
        return(boot_switch)




