if __name__ == '__main__':
    
    test_cases = int(input())
   
    for i in range(test_cases):
        entries = int(input())
        data = {}
        for i in range(entries):
            name, quantity  = input().split(" ")
            data[name] = int(quantity)

        operations = int(input())

        for i in range(operations):
            operation, name, quantity  = input().split(" ")
            quantity = int(quantity)

            if(name not in data.keys() and operation == "ADD" ):
                data[name] =quantity
                print(f"ADDED Item {name}")
                
            elif (name in data.keys()):
                value = data[name]
                if(operation == "ADD"):
                    value += quantity
                    print(f"UPDATED Item {name}")
                    
                elif(operation == "DELETE"):
                    if(value > quantity):
                        value -= quantity
                        print(f"DELETED Item {name}")
                    elif(value < quantity):
                        print(f"Item {name} could not be DELETED")

                    else:
                        print(f"Item {name} does not exist")
                data[name] =value

        total_items = 0    
        print(data)
        for key,values in data.items():
            total_items += values
        print(f"Total Items in inventory: {total_items}")
    
