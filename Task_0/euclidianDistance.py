def euc_dist(x1,y1,x2,y2):
    distance = (((x2-x1)**2)+((y2-y1)**2))**0.5
    print("distance: %0.2f"%distance)

entries = int(input())
for i in range(entries):
    x1,y1,x2,y2 = map(int, input().split(" "))
    euc_dist(x1,y1,x2,y2)

