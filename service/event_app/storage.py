import boto3
from uuid import uuid4
import base64


class Storage():
    def __init__(self) -> None:
        self.bucket_name = 'yandexcasebackendstorage'
        self.session = boto3.session.Session()
        self.s3 = self.session.client(service_name='s3',
                                     endpoint_url='https://storage.yandexcloud.net')
        
    def load_object_and_get_link(self, obj) -> str:
        storage_name = uuid4()
        storage_path = f'https://storage.yandexcloud.net/yandexcasebackendstorage/{storage_name}'

        self.s3.upload_file(obj, self.bucket_name, str(storage_name))

        return storage_path
    

if __name__ == '__main__':
    strg = Storage()
    obj_link = '-'

    with open('./silly.jpeg', 'rb') as file:
        obj_link = strg.load_object_and_get_link(obj='./silly.jpeg')
    print(obj_link)


