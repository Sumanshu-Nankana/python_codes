"""
In below we are creating three test cases for same function
"""

import pytest2

# def test_add():
#     assert pytest2.add(7,3) == 10

# def test_add_string():
#     result = pytest2.add('Hello',' World')
#     assert result == 'Hello World'
    
# def test_add_floar():
#     result = pytest2.add(10.5, 25.5)
#     assert result == 36

# ===============================================

"""
Another way is we can use assert commands in same test case
but still we are callinng add function 3 times
"""

# def test_add():
#     assert pytest2.add(7,3) == 10
#     result = pytest2.add('Hello',' World')
#     assert result == 'Hello World'
#     result = pytest2.add(10.5, 25.5)
#     assert result == 36

"""
"""

"""
Another way is parametrization
"""

import pytest

@pytest.mark.parametrize('var1, var2, result',
                        [
                            (7, 3, 10),
                            ('Hello',' World', 'Hello World'),
                            (10.5, 25.5, 36)
                        ]
                        )
def test_add(var1, var2, result):
    assert pytest2.add(var1,var2) == result
    