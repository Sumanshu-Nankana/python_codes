"""
Lets add the decorator @pytest.mark  and followed by any name
We have two markers now  number and strings
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
    assert pytest1.product(7) == 14
    
    
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
    
    
"""
Now, we can execute on basic of mark
"""