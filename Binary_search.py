def BinarySearch(L,k):
    left = 0
    right = len(L)-1
    while left<=right:
        mid = (left+right)//2
        if L[mid]==k:
            return mid
        elif L[mid]<k:
            left = mid+1
        else:
            right = mid -1
    return -1

if __name__=='__main__':
    arr = [1,2,3,5,4,6,7,8,9,13,11]
    k = int(input('Enter the key to search:'))
    result = BinarySearch(sorted(arr),k)
    if result>=0:
        print(k,'is found at index',result)
    else:
        print(k,'not exist in list')