def Linear_search(l,n):
    for i in range(len(l)):
        if l[i]==n:
            return i
    return -1
if __name__=='__main__':
    arr = [1,3,2,5,6,7,4,3,22]
    n = int(input('Enter value to check:'))
    result = Linear_search(arr,n)
    if result >= 0:
        print(n,'found at index',result)
    else:
        print(n,'not exist in list')