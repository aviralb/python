#break and continue stattement

i= 0
while("true"):
    if i+1<5:
        i=i+1
        continue

    print(i+1,end=" ")
    if(i==24):
        break
    i=i+1

input("bingo")