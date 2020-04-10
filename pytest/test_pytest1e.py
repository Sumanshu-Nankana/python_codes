"""
Let's add a failure and then we will use -x option to see if further test run or not run
So we added a failure in test_product function in line assert pytest1.product(7) == 13  
"""

import pytest1
import pytest


@pytest.mark.number
def test_add():
    assert pytest1.add(7, 3) == 10
    assert pytest1.add(7) == 9

@pytest.mark.number
def test_product():
    assert pytest1.product(5, 3) == 15
    assert pytest1.product(7) == 13  
    
    
@pytest.mark.strings
def test_add_strings():
    result = pytest1.add('Hello',' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Helo' not in result
    
@pytest.mark.strings
def test_product_strings():
    assert pytest1.product('Hello ',3) == 'Hello Hello Hello '
    result = pytest1.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
    