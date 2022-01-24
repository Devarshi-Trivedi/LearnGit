# sum of the even numbers in given range

# input
# it will take two int numbers as a range as firstelm, lastelm
# it will take two arguments as first=<int>, last=<int>, rng=<int>


def _chkValilator(tpl, dix):

    lst = [None, None, None]

    convertTonth = [
            ['first', 'first'],
            ['second', 'last'],
            ['third', 'rng']
    ]

    if tpl != ():
        
        for ind, val in enumerate(tpl):

            if ind >= len(convertTonth):
                break
            
            if not isinstance(val, int):
                raise Exception(f"this function needs {convertTonth[ind][0]} argument as integer")
            
            lst[ind] = val
            

    if dix != dict():

        for ind, sublist in enumerate( convertTonth):
            
            if sublist[1] in dix.keys():

                if not isinstance(dix[sublist[1]], int):
                    raise Exception(f"this function needs '{sublist[1]}' argument as an integer")

                lst[ind] = dix[sublist[1]]

  
    if sum([1 if i != None else 0 for i in lst]) < 2 :
        raise Exception(f"not enough value to perform task")
        
    return lst


def FindEvenSerSum(flist, *args, **kargs ):

    # input 
    if flist == None:
        raise Exception("this function needs list as a first argument")


    firstelm, lastelm, rng = _chkValilator(args, kargs)

    # process

    if firstelm != None:
        if firstelm % 2 != 0:
            firstelm += 1

        if rng != None:
            return int ((rng * (firstelm * 2 + (rng - 1 ) * 2))/2)

        else:
            lastelm = lastelm if lastelm % 2 == 0 else lastelm - 1

            return int((((lastelm - firstelm)/2) + 1) * (firstelm + lastelm) / 2 )

    else:

        if lastelm % 2 != 0:
            lastelm -= 1

        return int(rng * (lastelm * 2 - (rng - 1) * 2) / 2)




if __name__ == "__main__":
    print(FindEvenSerSum([], last=10, first=11))