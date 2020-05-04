'''
hacker-rank-problem:calculate mean,median and mode
of space separeted input data

N.B:..print 1 digit after fraction(if have)
'''


import statistics as st
n = int(input())
if n>=10 and n<=2500:
    arr = list(map(int,input().split()))
    arr = list(sorted(arr))

    mean = st.mean(arr)
    if len(arr)%2==0:
        median = (st.median_low(arr)+st.median_high(arr))/2
    elif len(arr)%2==1:
        median = st.median(arr)

    try:
        mode = st.mode(arr)
    except:
        pass
    else:
        mode = min(arr)

    print('%.1f'%mean)
    print('%.1f'%median)
    print(mode)
