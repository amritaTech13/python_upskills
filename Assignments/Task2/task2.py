import requests
from typing import Dict

url = 'https://reqres.in/api/users/2'

data = requests.get(url)
product_data = data.json()
# print(product_data)

def get_additional_data(style_number, sku_id,test_AM):
    additional_data_temp = {'style_number': style_number, 'sku_id': sku_id, 'testA':test_AM, 'support': "test_support_data"}
    return additional_data_temp

additional_data: Dict = get_additional_data("CWS10", 10,'test_AM')

def pre_process_data():
    # for field in additional_data:
    #     if field != 'support':
    #         product_data[field] = additional_data[field]
    # return product_data
    product_data.update({key:val for key, val in additional_data.items() if key != 'support'} )
    return product_data

print(pre_process_data())

