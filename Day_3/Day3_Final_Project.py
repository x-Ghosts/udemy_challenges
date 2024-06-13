# Main objective is to build up a story line based on a if/else and multiple conditions, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132?start=0#overview (Course enrolling is mandatory)



print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("\n")
print("Welcome to the Treasure Island !")
print("Your mission is to find and guess where the treasure is, based on your choices.")

print('''You're at a cross road. Where do you want to go ? Left or Right ? Type "Left" or "right".''')

choice = input()
if choice.lower() == 'right':
    print("You fall in a hole. Game over !")
else:
    print("Epic ! You moved away and found that there is a river on your way. But how to deal with it ? Do you wanna swim, or wait for a boat to pick you up ? Type 'swim' or 'wait'.")
    choice = input()
    if choice.lower() == 'swim':
        print("I wonder how you can survive in front of a group of hungry crocodiles :p. Game over !")
    elif choice.lower() == 'wait':
        print("Great choice ! Now, after reaching out to the other side of the river, there are  small houses in which, rumours says that treasure is hidden somewhere there.")
        print("There are 3 houses : Yellow House, Blue House and a Red House. You have only one choice to pick, which home you feel that the treasure is hiding in there ? Type 'red', 'blue' or 'yellow'." )
        choice = input()
        if choice.lower() == 'yellow' :
            print("Congratulations ! You found the treasure. Now close your eyes, and tells us how you imagined that treasure !")
        elif choice.lower() == 'red' or choice.lower() == 'blue':
            print("Oh no! You just fall in a trap and the doors are locked ! Good luck getting out and Game over !")
        else:
            print("We just told you that 3 homes just existed, you can't invent more ! Congratulations for your loss !!!")
    else:
        print("There is no way arround, do you know why ? Because someone knew you're looking for the valuable treasure, and they placed bounty at you, and you can't come back to them ! Game over !")