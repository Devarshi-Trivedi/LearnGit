# reverse string

class InvalidInputGiven(Exception):

    def __init__(self, message="input is not given as expected"):
        self.message = message

    def __str__(self):
        return self.message + ": error occured"


def inpvalidator(x = None):

    if x == None or not isinstance(x, str):
        raise InvalidInputGiven('String input needed insted ' + str(type(x)) + ' is given') 

    if x == '':
        raise InvalidInputGiven('Empty string is given')


if __name__=="__main__":
    print(inpvalidator('hello'))