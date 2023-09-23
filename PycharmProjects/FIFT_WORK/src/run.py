import requests
import os




def get_company(company_id):

    headers = {'User-Agent':'HH-User_Agent'}
    url = f'https://api.hh.ru/employers/{company_id}'
    response = requests.get(url, headers=headers)
    response = response.json()
    data = {'hh_id': response.get('id'),
            'name': response.get('name'),
            'descriptions': response.get('id'),
            'url_company': response.get('alternate_url')
    }
    return data

def get_vacancy():
        request = requests.get(self.url, params = self.params)
        return request
