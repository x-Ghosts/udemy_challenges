# Main objective is to build a successful code that fill in the needs of the requirements, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/17837506#overview (Course enrolling is mandatory)


# 1/ Create a Greeting for your program :

print("Welcome to the Band Name Generator.")

# 2/ Ask the user for the city where they grew up :
print("What's the name of the city you grew in ?")
city_name = input()

# 3/ Ask the user for the petname :
print("What's your pet's name ?")
pet_name = input()

# 4/ Combine the name of the city and the pet name and show their band name:
band_name = city_name + " " + pet_name
print("Your band name could be " + band_name)






### Alternative solution :

# 1/ Create a Greeting for your program :

print("Welcome to the Band Name Generator.")

# 2/ Ask the user for the city where they grew up :

city_name = input("What's the name of the city you grew in ?\n")

# 3/ Ask the user for the petname :

pet_name = input("What's your pet's name ?\n")

# 4/ Combine the name of the city and the pet name and show their band name:
band_name = city_name + " " + pet_name
print("Your band name could be " + band_name)