counter = 0
while counter < 5:
    var = int(input('Guess The Number:\n '))
    if var == 10:
        print('Congratulations, You have guessed the Secret number = 10 ')
        print('Number of attempts:  ', (counter+1))
        break
    elif var > 10:
        counter = counter+1
        print('The number is greater than secret number  ')
        print('Chances left: ', (-counter+5))
    elif var < 10:
        counter = counter+1
        print('The number is less then secret number ')
        print('Chances left: ', (-counter+5))

print("game over")
input("ab aur nahi ")