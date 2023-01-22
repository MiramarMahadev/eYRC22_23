if __name__ == '__main__':
    
    test_cases = int(input())

    for i in range(test_cases):
        students = []
        marks = []
        entries = int(input())
        for i in range(entries):
            name, score  = input().split(" ")
            students.append(name)
            marks.append(float(score))

        data = zip(students,marks)
        sort_mark = sorted(marks,reverse=True)

        topper = []

        for key ,value in data:
            if (value == sort_mark[0]):
                topper.append(key)
        topper = sorted(topper)
        for i in topper:
            print(i)
    




