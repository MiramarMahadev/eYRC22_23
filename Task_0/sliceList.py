
def slicer(size):
    x = list(map(int, input().split(" ")))
    
    for i in range(size):
        print(x[size-i-1],end=" ")
    print("")

    for i in range(1,size):
        if(i%3==0):
            print(x[i]+3,end=" ")
    print("")

    for i in range(1,size):
        if(i%5==0):
            print(x[i]-7,end=" ")
    print("")

    total = 0
    for i in list(x[3:8]):
        total += i
    print(total)


test_cases = int(input())

for i in range(test_cases):
    entries = int(input())
    slicer(entries)