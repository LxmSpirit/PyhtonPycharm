#coding:utf-8

'''
request参数
request就是我需要什么东西，用来接受参数，用到@pytest.fixture装饰器，
传参就用默认的request参数，user = request.param[] 这一步是接收传入的参数。

如果用到@pytest.fixture，里面用2个参数情况，可以把多个参数用一个字典去存储，这样最终还是只传一个参数。
不同的参数再从字典里面取对应key值就行，如： user = request.param[“user”]

'''

import pytest

login_data = [{'user': 'admin', 'password': '123456'}, {'user': 'admin', 'password': '1'}]

@pytest.fixture(scope='function')
def login(request):
    '''登录函数'''
    user = request.param['user']
    password = request.param['password']
    print('用户名：%s' % user)
    print('密码：%s' % password)
    return 'hello'



# 装饰器
@pytest.mark.parametrize('login',  login_data, indirect=True)
#indirect=True 参数是为了把login当作一个函数去执行，而不是一个参数
def test_login(login):
    #登录测试用例
    result = login
    assert result == 'hello'

if __name__ == '__main__':
    pytest.main(['-s', 'test_PytestRequest.py'])
