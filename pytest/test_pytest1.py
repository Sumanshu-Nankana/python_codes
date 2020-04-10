"""

Now we created test_pytest1 file to test the pytest1 code
This file should always start with test_
all functions should always be start with test_  (and no parameter will be passed into this)
So, that pytets module automatically detect it that these are pytest modules and which needs to be run

Let's import the pytest1 module first

So to test add() function in pytest we prepare two test cases
if we pass 7,3 we are expecting 10  - if 10 come, then test will passed, else it will failed.
if we pass only 7, we are expecting 9

Similarly we prepare test cases for product() function

Now, we have prepared the test cases - Now we will run all these using pytest
open terminal and use below command -

pytest test_pytest1.py

"""
import pytest1

def test_add():
    assert pytest1.add(7, 3) == 10
    assert pytest1.add(7) == 9
    
def test_product():
    assert pytest1.product(5, 3) == 15
    assert pytest1.product(7) == 14
    
    
"""
sumanshu@sumanshu-Lenovo-G50-80:~/Desktop/Python and ML - Self Learning/Python/pytest$ pytest test_pytest1.py 
============================== test session starts ==================================
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
rootdir: /home/sumanshu/Desktop/Python and ML - Self Learning/Python/pytest, inifile:
collected 2 items                                                                                                                            

test_pytest1.py ..                                                                                                                     [100%]

========================== 2 passed in 0.01 seconds================================
"""