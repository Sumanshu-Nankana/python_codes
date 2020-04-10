import logging

# This is to define a new logger ; so that if it get python file imported by some file
# then root logger settings not get overrite
# and we need to use logger (instead of logging - where ever we are logging the details

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('employee.log')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Employee:
    """A Sample Employee Class"""
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('Sumanshu','Nankana')
emp_2 = Employee('Ashish','Kumar')        
emp_3 = Employee('Rajesh','Arya')     