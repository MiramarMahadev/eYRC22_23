
def dec_to_binary(num):
    bcd=""
    rem = num%2
    if(num ==0):
        size = len(x)
        while(size < 8):
            x.append(0)
            size+=1
        x.reverse()
        for i in x:
            bcd += str(i)
        print(bcd)
    else:
        x.append(rem)
        dec_to_binary(num//2)

inputs = int(input())
for i in range(inputs):
    x =[]
    num = int(input())
    dec_to_binary(num)

