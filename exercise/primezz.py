def isPrime(n):
    if isinstance(n,int):
        if n ==2:
            return True
        elif n <2 or n%2==0:
            return False
        else:
            return isPrime([n,1,2])
    #turns input of the list to a list

    elif len(n) <= pow(n[0],0.5):
    #since im using the len of a list as the counter stop recursion eg when n = [5,1,2,3,4]
        if n[0]%len(n)==0:
            return False
        # if len of the list is a factor i add it the the list of factors
        else:
            return isPrime(n+[None,None])
        #if the len of list is not a factor i add 2 to the len of the list by adding 2 none values
    else:
        return True
        #reaches here if recursion ends and list has only 2 integers and the rest are none


print(isPrime(1299709))

