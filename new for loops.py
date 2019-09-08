items = [int,float,"ram",1,2,3,4,5,6,7,8,9,12,11,15,55,66,11]
for item in items:
    if str(item).isnumeric() and item>=7:
        print(item)

input("")