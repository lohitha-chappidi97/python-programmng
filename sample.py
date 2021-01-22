"'this is sample of creating module'"
def Is_Even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
    
def Is_prime(n):
    if n == 1:
        return False
    cnt = 0
    for i in range(2,n):
        if(n%i == 0):
            cnt+=1
            break
    if(cnt == 0):
        return True
    else:
        return False


def prime_gen(a,b):
    for i in range(a,b+1):
        if Is_prime(i):
            print(i)



def Is_perfect(n):
    fc=0
    for i in range(1,n):
        if(n%i==0):
            fc+=i
    if(fc==n):
        return True
    else:
        return False