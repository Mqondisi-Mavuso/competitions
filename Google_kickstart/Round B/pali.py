def palins():
    n=0
    while True:
        n+=1
        m=(n+1)//2
        for i in range(10**(m-1),10**m):
            if n%2==1:
                yield int(str(i)+str(i)[-2::-1])
            else:
                yield int(str(i)+str(i)[::-1])

for case in range(1,int(input())+1):
    p=palins()
    n=int(input())
    m=0
    while True:
        t=next(p)
        if t>n or t>=10**5:break
        if n%t==0:m+=1
    for k in range(1,10**5):
        if n%k==0 and n//k>=10**5 and str(n//k)==str(n//k)[::-1]:m+=1
    print('Case #',case,': ',m,sep='')