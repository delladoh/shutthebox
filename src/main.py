from numbox import *
from dice import *


print("Welcome to shut the box!")

total = 78
gameover = False
while not gameover:
    player = input("Would you like to contune playing? (yes/no) ").lower()
    
    if player == "no":
        print("You have quit.")
        break
    else:
        for i in numbox:
         if i != "e":
            print(i, end=" ")
        dice1 = roll_dice()
        dice2 = roll_dice()
        dicetotal = dice1 + dice2
        print("\nDice 1: " + str(dice1))
        print("Dice 2: " + str(dice2))

        if dicetotal > total:
           print("Game Over- You Lose! Yur end total is " + total)
           break

        success = False
        while not success:
            eliminate = input("Would you like to elimiate 1 or 2 boxes? ")
            if eliminate == "1":
                number = 0
                valid = True
                while number not in [2,3,4,5,6,7,8,9,10,11,12] and valid == True:
                    number = int(input("Enter the number you wish to elimate: "))
                if number == dicetotal and numbox[number-1] != "e" and number <= total:
                    print("Success!")
                    numbox[number-1] = "e"
                    total -= number
                    success = True
                elif numbox[number-1] == "e":
                    valid = False
                    print("Invalid input: {} is not available. Try again!".format(number))
                else:
                    valid = False
                    print("Invalid input")   
            else: 
            # check permutation in possible
            # loop true and create a list of available  permutations
                permutation = [0,0,0,0,0,0,0,0,0,0,0,0]
                temp1 = 0
                for i in numbox:
                    temp2 = 0
                    temp1 += 1
                    if i != "e":
                      for j in numbox:
                        
                        temp2 += 1
                        if j != "e" and temp1 != temp2 and temp1+temp2<=12:
                            temp = temp1+temp2
                            permutation[temp-1] = 1

                if permutation[dicetotal-1] == 0:
                    print("Game Over! You Lose! Your final total is {}".format(total))
                    gameover = True
                    break

                number1=0
                number2=-1
                valid = True
                while number1 not in [2,3,4,5,6,7,8,9,10,11,12] and number2 not in [2,3,4,5,6,7,8,9,10,11,12] and number1!=number2:
                    number1 = int(input("Enter the number you wish to elimate: "))
                    number2 = int(input("Enter the number you wish to elimate: "))
                    if number1 == number2:
                        print("Your choice of numbers can not be the same, try again!")
                numberTotal = number1 + number2
                if numberTotal == dicetotal and numbox[number1-1] != "e" and numbox[number2-1] != "e" and numberTotal <= total:
                        print("Success!")
                        numbox[number1-1] = "e"
                        numbox[number2-1] = "e"
                        total -= numberTotal
                        success = True
                elif numbox[number1-1] == "e":
                        valid = False
                        print("Invalid input: {} is not available. Try again!".format(number1)) 
                elif numbox[number2-1] == "e":
                        valid = False
                        print("Invalid input: {} is not available. Try again!".format(number2))
                elif numberTotal != dicetotal:
                        valid = False
                        print("Invalid input: {} is not equal to the dice total. Try again!".format(number))
                else:
                        valid = False
                        print("Invalid input") 
            
        if total == 0:
           print("Game Over! You Win!!!!! :)")
           break

              
        
        


print("Thank you for playing!")