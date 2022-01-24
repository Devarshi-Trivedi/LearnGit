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
        lst.push(arg[1])
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


    
    

    