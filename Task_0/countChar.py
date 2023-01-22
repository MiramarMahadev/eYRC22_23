def count_char(line):
    lis = list(line.split(" "))
    for i in range(len(lis)):
        size = len(lis[i])
        if i ==0:
            size -= 1
        if i == len(lis)-1:
            print(size)
        else:
            print(size,end=",")

entries = int(input())
for i in range(entries):
    sent = input()
    count_char(sent)