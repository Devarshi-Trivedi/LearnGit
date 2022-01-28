# list operation

def giveInstOfError(stment):
    print(stment)
    exit()

def listop(lst=None, opcode=None, *arg ):
    
    if lst == None or not isinstance(lst, list):
        giveInstOfError('listop needs first argument as list')

    if opcode == None:
        giveInstOfError('listop needs second argument as operation instruction')
        
    if not isinstance(opcode, str):
        giveInstOfError('listop needs second argument as operation instruction in string type')


    if opcode == 'clear':
        lst = []
        return lst

    if opcode == 'push':
        if len(arg) == 0:
            giveInstOfError('no element for push operation')
        lst.append(arg[0])
        return {
            'index': len(lst) - 1,
            'val': arg[0],
            'list': lst,
        }
    
    if opcode == 'shift':
        if len(arg) == 0:
            giveInstOfError('no element for shift operation')
        lst.insert(0, arg[0])
        return {
            'index': 0,
            'val': arg[0],
            'list': lst,
        }

    if opcode == 'pop':
        if lst == []:
            giveInstOfError('pop operation can not be perform on empty list')
        return {
            'index': len(lst) - 1,
            'val': lst.pop(),
            'list': lst
        }

    if opcode == 'unshift':
        if lst == []:
            giveInstOfError('unshift operation can not be perform on empty list')
        return {
            'index': 0,
            'val': lst.pop(0),
            'list': lst
        }

    if opcode == 'insert':
        if len(arg) < 2 or arg[1] == None or arg[0] == None:
            giveInstOfError('not enough arguments for insert operation')
        if not isinstance(arg[0], int):
            giveInstOfError('index should be in integer type')
        if arg[0] < 0 or arg[0] > len(lst):
            giveInstOfError('your given index is out of bound')

        

        lst.insert(arg[0], arg[1])
        return {
            'index': arg[0],
            'val': arg[1],
            'list': lst
        }

    if opcode == 'countdix':
        if lst == None:
            giveInstOfError('countdix can not perform on empty list')
        mydix = {}

        for i in lst:
            if i in mydix.keys():
                mydix[i] += 1
            else:
                mydix[i] = 1

        return {
            'list': lst,
            'setlist': list(mydix.keys()),
            'dict': mydix
        }