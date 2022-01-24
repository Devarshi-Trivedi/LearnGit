# reverse string
import re


class InvalidInputGiven(Exception):

    def __init__(self, message="input is not given as expected"):
        self.message = message

    def __str__(self):
        return self.message + ': error occured'


def inpvalidator(x = None):

    try:

        if x == None or x == '' or re.search('^[ ]+$', x):
            raise InvalidInputGiven('inpvalidator needs non empty string argument')

        if not isinstance(x, str):
            raise InvalidInputGiven('inpvalidator is looking for string argument instade argument with type ' + str(type(x)) + ' is given')

    except Exception as e:
        print(e)
        return False

    else:
        return True

    

def revString(x):

    return x[::1]


while(1):

    k = input()
    if inpvalidator(k):
        print(revString(k), 'stop')
        break