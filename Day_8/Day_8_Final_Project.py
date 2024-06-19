# Main objective is to create a program that encode and decode a message using ceaser cypher, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/19211072#overview (Course enrolling is mandatory)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shifted_alphabet = alphabet.copy()
encoded_output = []


direction = input("Type 'encode' to encrypt, or decode to 'decrypt': \n")
text = input("Write the message: \n").lower()
shift = int(input("Type the shift number: \n"))



'''def encrypt(text, shift):
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            print(index)
            new_alphabet = alphabet[index + shift]
            new_format.append(new_alphabet)
    print(new_format)'''

def encrypt2(text,shift):
    count = 0
    while not count == shift:
        for i in range (0, shift,1):
            count += 1
            letter = shifted_alphabet.pop(0)
            shifted_alphabet.append(letter)
    #For purpose of checking if things goes good
    print(alphabet)
    print(shifted_alphabet)
    '''for letters in alphabet:
        for msg_letter in text:
            if msg_letter == letters:
                letter_index = alphabet.index(letters)
                encoded_letter = shifted_alphabet[letter_index]
                encoded_output.append(encoded_letter)'''
    for letters in text:
        index = alphabet.index(letters)
        encoded_letter = shifted_alphabet[index]
        encoded_output.append(encoded_letter)
    print(encoded_output)

        


if direction.lower() == 'encode':
    encrypt2(text, shift)