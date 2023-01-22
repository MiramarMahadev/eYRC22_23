def pattern(num):
    lis = []
    for i in range(1,num+2):
        if(i%5 == 0):
            lis.append("#")
        else:
            lis.append("*")
    for i in range(1,num+1):  
        lis.pop()
        for i in lis:
            print(i,end="")
        print("")

inputs = int(input())
for i in range(inputs):
    step = int(input())
    pattern(step)