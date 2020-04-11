#
# Pylint Tutorial
#

"""Pylint Practice"""

class Car(object):
    """Example Docstring"""
    def __init__(self, color):
        self.color = color

MY_CAR = Car('blue')

def crash(car1, car2):  #pylint: disable=unused-argument
    """Example Fun Docstring"""
    car1.color = 'burnt'

crash(Car('red'), MY_CAR)
