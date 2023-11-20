#coding=utf-8

import pytest

@pytest.mark.webtest
def test_send_http():
    print('test_send_http')
    pass

@pytest.mark.apptest
def test_something_quick():
    #print('test_something_quick')
    pass

def test_another():
    #print('test_another')
    pass

def add(a,b):
    return a+b

class TestClass:
    def test_method(self):
        pass
    def test_add2(self):
        assert 5 == add(1, 4)


if __name__=='__main__':
    #pytest.main(["-s","test_PytestWebtest.py","-m=@pytest.mark.apptest"])
    pytest.main(["test_PytestWebtest.py::test_another","-v" ])