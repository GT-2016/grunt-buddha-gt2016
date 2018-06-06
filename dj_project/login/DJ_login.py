# coding:utf-8
import requests

class DJLogin(object):
    """
    Django 制作登录页面测试web请求
    """
    def __init__(self, url):
        '''初始化函数，传入参数 url'''
        self.url = url


    def get_url(self):
        '''get 方法'''
        dj = requests.get(self.url)
        return dj

    def post_url(self):
        param = {
            "user": "123",
            "passwd": "hello",
            "csfrmiddlewaretoken":"EG67FRmit7WvQjC8rfZFjR7S6mbfszhy"
        }

        dj = requests.post(self.url, params=param)
        return dj

if __name__ == '__main__':
    url = 'http://127.0.0.1:8001/index/'
    DJ = DJLogin(url)
    result = DJ.post_url()
    print(result)

