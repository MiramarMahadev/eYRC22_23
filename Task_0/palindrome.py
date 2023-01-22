def check_pal(str):
    size = len(str)
    rev = list()
    str = str.lower()
    for i in range(size):
        rev.append(str[size-1-i])
    if list(str) == rev:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
        
        
entries = int(input())
for i in range(entries):
    word = input()
    check_pal(word)
