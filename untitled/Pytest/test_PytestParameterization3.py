#coding=utf-8

import pytest

test_user_data1 = [
    {'user':'linda','password':'888888'},
    {'user':'servenruby','password':'123456'},
    {'user':'test01','password':'1'}

]

test_user_data2=[
    {'q':'中国平安','count':'3','page':'1'},
    {'q':'阿里巴巴','count':'2','page':'2'},
    {'q':'pdd','count':'3','page':'1'}

]

@pytest.fixture(scope='module')
def login_r(request):
    user = request.param['user']
    pwd = request.param['password']
    print('\n用户名：%s,密码：%s'%(user,pwd))


@pytest.fixture(scope='module')
def query_param(request):
    q = request.param['q']
    count = request.param['count']
    page = request.param['page']
    print('查询的搜索词%s'%q)
    return request.param

#pytest数据驱动，indirect=True是把login_r当作函数去执行
#从下往上执行???????????????
#两个数据进行组合测试，有3*3个测试用例执行
@pytest.mark.parametrize('login_r',test_user_data1,indirect=True)
@pytest.mark.parametrize('query_param',test_user_data2,indirect=True)
def test_login(query_param,login_r):
    #登录用例
    print(login_r)
    print(query_param)
