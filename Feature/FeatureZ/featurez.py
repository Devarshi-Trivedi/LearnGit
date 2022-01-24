# list operation

def giveInstOfError(stment):
    print(stment)
    exit()

def inpvalidater(lst=None, *arg ):
    
    if lst == None or not isinstance(lst, list):
        giveInstOfError('inpvalidater needs first argument as list')

    if len(arg) == 0:
        giveInstOfError('inpvalidater needs second argument as operation instruction')
        
    if isinstance(arg[0], str):
        giveInstOfError('inpvalidater needs second argument as operation instruction in string type')

    
    

    