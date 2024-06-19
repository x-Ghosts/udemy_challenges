# Main objective is to create a program that encode and decode a message using ceaser cypher, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/19211072#overview (Course enrolling is mandatory)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_format = []


direction = input("Type 'encode' to encrypt, or decode to 'decrypt': \n")
text = input("Write the message: \n").lower()
shift = int(input("Type the shift number: \n"))


def encrypt(text, shift):
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            print(index)
            new_alphabet = alphabet[index + shift]
            new_format.append(new_alphabet)
    print(new_format)


if direction.lower() == 'encode':
    encrypt(text, shift)