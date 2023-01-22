def series(num):
    for i in range(num):
        if i ==0:
            print(i+3,end=" ")
        elif i%2 ==0:
            if i ==num-1:
                print(2*i)
            else:
                print(2*i,end=" ")
        else:
            if i ==num-1:
                print(i**2)
            else:
                print(i**2,end=" ")

entries = int(input())
for i in range(entries):
    num = int(input())
    series(num)