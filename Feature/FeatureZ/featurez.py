# list operation

def giveInstOfError(stment):
    print(stment)
    exit()

def listop(lst=None, *arg ):
    
    if lst == None or not isinstance(lst, list):
        giveInstOfError('listop needs first argument as list')

    if len(arg) == 0:
        giveInstOfError('listop needs second argument as operation instruction')
        
    if isinstance(arg[0], str):
        giveInstOfError('listop needs second argument as operation instruction in string type')


    if arg[0] == 'clear':
        lst = []
        return lst

    if arg[0] == 'push':
        if len(arg) < 2:
            giveInstOfError('no element for push operation')
        lst.append(arg[1])
        return {
            'index': len(lst) - 1,
            'val': arg[1],
            'list': lst,
        }
    
    if arg[0] == 'shift':
        if len(arg) < 2:
            giveInstOfError('no element for shift operation')
        lst.insert(0, arg[1])
        return {
            'index': 0,
            'val': arg[1],
            'list': lst,
        }

    if arg[0] == 'pop':
        if lst != []:
            giveInstOfError('pop operation can not be perform on empty list')
        return {
            'index': len(lst) - 1,
            'val': lst.pop(),
            'list': lst
        }

    if arg[0] == 'unshift':
        if lst != []:
            giveInstOfError('unshift operation can not be perform on empty list')
        return {
            'index': 0,
            'val': lst.pop(0),
            'list': lst
        }

    if arg[0] == 'insert':
        if len(arg) < 3 or arg[2] == None:
            giveInstOfError('not enough arguments for insert operation')
        if not isinstance(arg[1], int):
            giveInstOfError('index should be in integer type')
        if 0 > arg[1] > len(lst):
            giveInstOfError('your given index is out of bound')

        lst.insert(arg[1], arg[2])
        return {
            'index': arg[1],
            'val': arg[2],
            'list': lst
        }

    
    
    

    