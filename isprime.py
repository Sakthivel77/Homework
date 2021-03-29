def isPrime(n):
    # since 1 is not a prime
    if n == 1:
        return False
    elif isinstance(n,int):
        return isPrime([n,1])
    #turns input of the list to a list

    elif len(n) != n[0]:
    #since im using the len of a list as the counter stop recursion eg when n = [5,1,None,None,None]
        if n[0]%len(n)==0:
            return False
        # if len of the list is a factor i add it the the list of factors
        else:
            return isPrime(n+[None])
        #if the len of list is not a factor i add None the the list
    else:
        return True
        #reaches here if recursion ends and list has only 2 integers and the rest are none


print(isPrime(541))
