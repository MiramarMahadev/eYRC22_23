from functools import reduce

def generate_AP(a1, d, n):
    AP_series = []
    for i in range(n):
        term = a1+ i*d
        AP_series.append(term)

    return AP_series

if __name__ == '__main__':
    
    test_cases = int(input())

    for i in range(test_cases):
        a1, d, n = map(int, input().split(" "))

        AP_series = generate_AP(a1, d, n)
        size_ap = len(AP_series)
        for i in range(size_ap):
            if(i==size_ap-1):
                print(AP_series[i])
            else:
                print(AP_series[i],end=" ")
    
        sqr_AP_series = list(map(lambda x: x*x,AP_series))
    
        size_sqap = len(sqr_AP_series)
        
        for i in range(size_sqap):
            if(i==size_sqap-1):
                print(sqr_AP_series[i])
            else:
                print(sqr_AP_series[i],end=" ")
    
    
        sum_sqr_AP_series = reduce(lambda x,y: x+y, sqr_AP_series)
    
        print(sum_sqr_AP_series)