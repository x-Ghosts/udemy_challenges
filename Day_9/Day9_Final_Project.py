# Main objective is to create a program that does a blind auction, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/19279394#overview (Course enrolling is mandatory)

from ascii_art import logo
from os import system

auction_list = []

print(logo + "\n")
name = input("What's your name ? ")
bid = float(input("What's your bid ? $"))
stop_program = False




def bid_input(name, bid):
    auction = {}
    auction['name'] = name.title()
    auction['bid'] = int(round(bid))
    auction_list.append(auction)
    print(auction)

bid_input(name, bid)

while stop_program == False:
    multiple_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if multiple_bidders.lower() == 'yes':
        system('cls') #this for clearing the page, because I'm coding directly via VSCode
        name = input("What's your name ? ")
        bid = float(input("What's your bid ? $"))
        bid_input(name, bid)
    
    elif multiple_bidders.lower() == 'no':
        system('cls')
        auction_max_value = 0
        for i in range (0, len(auction_list)):
            if auction_list[i]['bid'] > auction_max_value:
                index_max = i
                auction_max_value = auction_list[i]['bid']
        print(f"The winner is {auction_list[index_max]['name']} with ${auction_max_value}.")
        stop_program = True