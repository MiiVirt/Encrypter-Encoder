import numpy as np

file_path = "data.txt"

#TODO Handling if less than 32 or over 126 (loop unicode)
#TODO Error handling for empty input and negative keys
#TODO menu inprovement
#TODO function that converts to unicode/char
#TODO Key value can be anything and will be converted into sum of unicode

def Unicode(value):
    #loop unicode if it goes bellow 32
    if value < 32:
        return 126 - (31 - value) % 95
    elif value > 126:
        return 32 + (value - 127) % 95
    else:
        return value
def Encrypting():

    data = input("Data")

    #Check if key is int
    while True:
        try:
            key = int(input("Key (number)"))
            break
        except ValueError:
            print("Invalid input. Enter a round number as key")

    #Convert data to unicode
    datalist = np.array([ord(character) for character in data])

    #Convert key to integrer
    intkey = int(key)

    # Encryption and loop Unicode values within printable ASCII range
    encrypted_data = ''.join([chr(Unicode(value - intkey)) for value in datalist])

    #Save the data to a data.txt file
    with open(file_path, 'w') as file:
        file.write(encrypted_data)

    print("Encrypted data", encrypted_data)

def Encoding():

    #data = input("Encrypted data")
    with open(file_path, 'r') as file:
        data = file.read()

    #Check if key is int
    while True:
        try:
            key = int(input("Key (number)"))
            break
        except ValueError:
            print("Invalid input. Enter a round number as key")

    #Convert data to unicode
    datalist = np.array([ord(character) for character in data])

    #Convert key to integerer
    intkey = int(key)

    # Loop Unicode values within printable ASCII range
    decoded_data = ''.join([chr(Unicode(value + intkey)) for value in datalist])

    print("Decrypted data", decoded_data)

def Main():
    print("Are you trying to encrypt your data or encode your encrypted data?")
    x = input("Type '1' if you wish to encrypt, type '2' to encode or '3' to exit")

    if x == "1":
        Encrypting()
    elif x== "2":
        Encoding()
    else:
        print("Exiting")

Main()
