"""

Let's remove test_ prefix from test function and use some other prefix

"""
import pytest1

def t_add():
    assert pytest1.add(7, 3) == 10
    assert pytest1.add(7) == 9
    
def test_product():
    assert pytest1.product(5, 3) == 15
    assert pytest1.product(7) == 14
    
    
"""
We could notice it only identify test_product as a test case
 
============================= test session starts ==============================
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
rootdir: /home/sumanshu/Desktop/Python and ML - Self Learning/Python/pytest, inifile:
collected 1 item                                                               

test_pytest1b.py .                                                       [100%]

=========================== 1 passed in 0.05 seconds ===========================

In verbose mode 

============================= test session starts ==============================
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python2
cachedir: .cache
rootdir: /home/sumanshu/Desktop/Python and ML - Self Learning/Python/pytest, inifile:
collected 1 item                                                               

test_pytest1b.py::test_product PASSED                                    [100%]

=========================== 1 passed in 0.01 seconds ===========================

"""