import pytest1

def test_add():
    assert pytest1.add(7, 3) == 10
    assert pytest1.add(7) == 9
    
def test_product():
    assert pytest1.product(5, 3) == 15
    assert pytest1.product(7) == 14
    
def test_add_strings():
    result = pytest1.add('Hello',' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Helo' not in result
    
def test_product_strings():
    assert pytest1.product('Hello ',3) == 'Hello Hello Hello '
    result = pytest1.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
    
"""
============================= test session starts ==============================
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python2
cachedir: .cache
rootdir: /home/sumanshu/Desktop/Python and ML - Self Learning/Python/pytest, inifile:
collected 4 items                                                              

test_pytest1c.py::test_add PASSED                                        [ 25%]
test_pytest1c.py::test_product PASSED                                    [ 50%]
test_pytest1c.py::test_add_strings PASSED                                [ 75%]
test_pytest1c.py::test_product_strings PASSED                            [100%]

=========================== 4 passed in 0.03 seconds ===========================
"""
    