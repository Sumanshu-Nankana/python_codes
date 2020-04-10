"""

Let's expect some enexpected value

"""
import pytest1

def test_add():
    assert pytest1.add(7, 3) == 10
    assert pytest1.add(7) == 9
    assert pytest1.add(5) == 9
    
def test_product():
    assert pytest1.product(5, 3) == 15
    assert pytest1.product(7) == 14
    
    
"""
We could notice 1 test pass and 1 test failed.
as we are expeting 9, but output is 7 - thus 1 test passed and 1 test faile

============================= test session starts ==============================
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
rootdir: /home/sumanshu/Desktop/Python and ML - Self Learning/Python/pytest, inifile:
collected 2 items                                                              

test_pytest1_1.py F.                                                     [100%]

=================================== FAILURES ===================================
___________________________________ test_add ___________________________________

    def test_add():
        assert pytest1.add(7, 3) == 10
        assert pytest1.add(7) == 9
>       assert pytest1.add(5) == 9
E       assert 7 == 9
E        +  where 7 = <function add at 0x7f380910b350>(5)
E        +    where <function add at 0x7f380910b350> = pytest1.add

test_pytest1_1.py:11: AssertionError
====================== 1 failed, 1 passed in 0.11 seconds ======================

"""