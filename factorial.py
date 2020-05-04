def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)

if __name__=='__main__':
    n = int(input())
    result = factorial(n)
    print(n,'factorial is =',result)