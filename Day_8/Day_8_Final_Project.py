# Main objective is to create a program that encode and decode a message using ceaser cypher, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/19211072#overview (Course enrolling is mandatory)

from logo import logo

print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
shifted_alphabet = alphabet.copy()
encoded_output = []
decoded_output = []



direction = input("Type 'encode' to encrypt, or 'decode' to decrypt: \n")
text = input("Write the message: \n").lower()
shift = int(input("Type the shift number: \n"))



'''def encrypt(text,shift):
    count = 0
    encoded_message = ''
    while not count == shift:
        for i in range (0, shift,1):
            count += 1
            letter = shifted_alphabet.pop(0)
            shifted_alphabet.append(letter)
    for letters in text:
        if letters in alphabet:
            index = alphabet.index(letters)
            encoded_letter = shifted_alphabet[index]
            encoded_output.append(encoded_letter)
        else:
            index = text.index(letters)
            encoded_output.insert(index, letters)
    
    encoded_message = encoded_message.join(encoded_output)
    print(f"The encoded message is {str(encoded_message)}.")

def decrypt(text, shift):
    count = 0
    decoded_message = ''
    while not count == shift:
        for i in range (0, shift):
            count += 1
            letter = shifted_alphabet.pop()
            shifted_alphabet.insert(0,letter)
    for letters in text:
        if letters in shifted_alphabet:
            index = alphabet.index(letters)
            decoded_letter = shifted_alphabet[index]
            decoded_output.append(decoded_letter)
        else:
            index = text.index(letters)
            decoded_output.insert(index, letters)

    print(decoded_output)
    decoded_message = decoded_message.join(decoded_output)
    print(f"The decoded message is {str(decoded_message)}.")'''

def caeser(direction, text, shift):
    count = 0
    encoded_message = ''
    decoded_message = ''
    if direction.lower() == 'encode':
        while not count == shift:
            for i in range (0, shift,1):
                count += 1
                letter = shifted_alphabet.pop(0)
                shifted_alphabet.append(letter)
        for letters in text:
            if letters in alphabet:
                index = alphabet.index(letters)
                encoded_letter = shifted_alphabet[index]
                encoded_output.append(encoded_letter)
            else:
                index = text.index(letters)
                encoded_output.insert(index, letters)
    
        encoded_message = encoded_message.join(encoded_output)
        print(f"The encoded message is {str(encoded_message)}.")

    elif direction.lower() == 'decode':
        while not count == shift:
            for i in range (0, shift):
                count += 1
                letter = shifted_alphabet.pop()
                shifted_alphabet.insert(0,letter)
        for letters in text:
            if letters in shifted_alphabet:
                index = alphabet.index(letters)
                decoded_letter = shifted_alphabet[index]
                decoded_output.append(decoded_letter)
            else:
                index = text.index(letters)
                decoded_output.insert(index, letters)

        decoded_message = decoded_message.join(decoded_output)
        print(f"The decoded message is {str(decoded_message)}.")


caeser(direction, text, shift)
