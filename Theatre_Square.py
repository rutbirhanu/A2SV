
def square(n,m,a):
    count=count1=1
    first=n%a
    second=m%a
    if first!=0:
        count1=n//a+1
    else:
        count1=n/a
    if second!=0:
        count=m//a+1
    else:
        count=m/a
    print(int(count*count1))

value = input().split()
n = int(value[0])
m = int(value[1])
a = int(value[2])

square(n,m,a)