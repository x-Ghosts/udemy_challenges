#####################################################
"""             Difficult Challenge               """
#####################################################




# Main objective is to create a program that will mark a spot on a map with an "X", according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101270#overview (Course enrolling is mandatory)


line1 = ["□","□","□"]
line2 = ["□","□","□"]
line3 = ["□","□","□"]
map = [line1, line2, line3] #nested list

print("Hiding your treasure ! 'X' makes the spot.")
position = input() #They give only 2 information (A,B,C in columns) and (1,2,3 for rows). However, we will use the position[0] to tell that its the column and position[1] that its row

# TIP : Always convert to check what type of data we work on.
print(type(position[0]))
print(type(position[1]))

# TIP : Create a copy of position that will hold the index of the the MAP list : MAP[A(position_copy = 0) or B(position_copy = 1) or C(position_copy = 2)][Second String part - 1]
if position[0].upper() == "A":
    position_copy = 0
elif position[0].upper() == "B":
    position_copy = 1
elif position[0].upper() == "C":
    position_copy = 2
else:
    print("Treasure out of map !")
'''
if (position[0]) == "A":
    map[position[0]] = 0
elif (position[0]) == "B" :
    map[position[0]] = 1
elif (position[0]) == "C" :
    map[position[0]] = 2
'''
map[position_copy][int(position[1])-1] = 'X'


print(f"{line1}\n{line2}\n{line3}")