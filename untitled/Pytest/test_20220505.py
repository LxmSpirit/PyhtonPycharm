#coding=utf-8
import pytest
# fixtures documentation order example

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

'''
fixture装饰的函数入参，只能是其他fixture。
'''

order = []
@pytest.fixture(scope="session")
def s1():
    order.append("s1")

@pytest.fixture(scope="module")
def m1():
    order.append("m1")

@pytest.fixture
def f1(f3):#fixture装饰的函数入参，只能是其他fixture。
    order.append("f1")
'''
@pytest.fixture
def f3():
    order.append("f3")
'''
@pytest.fixture(autouse=True)
def a1():
    order.append("a1")

@pytest.fixture
def f2():
    order.append("f2")

@pytest.fixture
def f3():
    order.append("f3")

def test_order(f1, m1, f2, s1):
    assert order == ["s1", "m1", "a1", "f3", "f1", "f2"]
    #虽然test_order()是按f1, m1, f2, s1调用的，但是结果却不是按这个顺序