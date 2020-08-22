
import random

nums = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

lower_letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

upper_letters = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

special_characters = [ '_', '@', '.', '-' ]

picker = [1, 2, 3, 4]

#check random.sample

def generate():
    password = ''
    user_lenght = int(input('Choose the lenght of your password (From 8 to 16): '))
    print('')
    
    for i in range(user_lenght):
        i = 0
        x = random.choice(picker)
        if x == 1:
           y = str(random.choice(nums))
           password += y
        elif x == 2:
           y = str(random.choice(lower_letters))
           password += y
        elif x == 3:
           y = str(random.choice(upper_letters))
           password += y
        elif x == 4:
           y = str(random.choice(special_characters))
           password += y
        i += 1
        
    print(password)
    print('Type yes to generate another password or type quit to close the program')
    again = input()
    if again == 'yes':
        print('')
        generate()
    elif again == 'quit':
        return

        
print('Password Generator')
print('')
print('Type start to generate a random password.')
user_inp = input()


if user_inp == 'start':
   generate()

    
 
