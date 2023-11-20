#conding=utf-8

import pytest
import logging

@pytest.mark.run(order=1)
def test_01():
    print('test01')
    assert True

@pytest.mark.run(order=2)
def test_02():
    print('test02')
    assert True

def test_06():
    print('test06')
    assert True

def test_04():
    print('test04')
    assert True

def test_05():
    print('test05')
    assert True

@pytest.mark.run(order=3)
def test_03():
    print('test03')
    assert True

'''
if __name__ == '__main__':
    pytest.main(['-s', 'test_PytestOrdering.py'])
'''