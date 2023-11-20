#coding=utf-8
'''
@pytest.fixture(scope='module')默认是function,可选择function,class,module,package或session
fixture 都是在test第一次调用时创建，根据scope的不同有不同的运行和销毁方式

function每个函数运行一次，函数结束时销毁
class每个类运行一次，类结束时销毁
module每个模块运行一次，模块结束时销毁
package每个包运行一次，包结束时销毁
session每个会话运行一次，会话结束时销毁

fixture的顺序优先按scope从大到小
session > package > module > class > function

如果scope相同，就按test调用先后顺序，以及fixture之间的依赖关系
autouse的fixture会优先于相同scope的其他fixture

'''

import pytest

@pytest.fixture(scope='module',autouse=True)
def start(request):
    print("\n--开始执行module--")
    print('module:%s'%request.module.__name__)
    print("----启动浏览器----")
    yield
    print("----结束测试 end!-----")

@pytest.fixture(scope="function",autouse=True)
def open_home(request):
    print("function:%s \n--回到首页--"% request.function.__name__)

def test_01():
    print('---用例01---')

def test_02():
    print('---用例02---')


if __name__=='__main__':
    pytest.main(["-s","test_PytestAutouse.py"])