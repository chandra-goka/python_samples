import math

def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    for i in range(2,(int)(math.sqrt(n))+1):
        if(prime[i] == True):
            j=i*i
            while j<=n :
                prime[j] = False
                j = j+i

    #printing all the prime numbers less than n
    for i in range(2,n+1):
        if(prime[i] == True):
            print (i, end=" ")


if __name__ == "__main__":
    n = int(input("Enter a number : "))
    SieveOfEratosthenes(n)
