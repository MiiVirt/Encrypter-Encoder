import numpy as np

file_path = "data.txt"

#TODO Error handling for empty input and negative int
#TODO menu inprovement
#TODO function that converts to unicode/char
#TODO Key value can be anything and will be converted into unicode

def Unicode_loop(value):
    # loop unicode if it goes bellow 32
    if value < 32:
        return 126 - (31 - value) % 95
    elif value > 126:
        return 32 + (value - 127) % 95
    else:
        return value
def Encrypting(z):

    # Check if the data will come from data.tx file or via input
    if z == 0:
        data = input("Data")
    else:
        with open(file_path, 'r') as file:
            data = file.read()

    # Check if key is int
    while True:
        try:
            key = int(input("Key (number)"))
            break
        except ValueError:
            print("Invalid input. Enter a round number as key")

    # Convert data to unicode
    datalist = np.array([ord(character) for character in data])

    # Convert key to int
    intkey = int(key)

    # Encryption and loop Unicode values within printable ASCII range
    encrypted_data = ''.join([chr(Unicode_loop(value - intkey)) for value in datalist])

    # Save the data to a data.txt file
    with open(file_path, 'w') as file:
        file.write(encrypted_data)

    print("Encrypted data", encrypted_data)

def Decoding():

    # data = input("Encrypted data")
    with open(file_path, 'r') as file:
        data = file.read()

    # Check if key is int
    while True:
        try:
            key = int(input("Key (number)"))
            break
        except ValueError:
            print("Invalid input. Enter a round number as key")

    # Convert data to unicode
    datalist = np.array([ord(character) for character in data])

    # Convert key to int
    intkey = int(key)

    # Loop Unicode values within printable ASCII range
    decoded_data = ''.join([chr(Unicode_loop(value + intkey)) for value in datalist])

    print("Decrypted data", decoded_data)

def Main():
    print("Are you trying to encrypt your data or encode your encrypted data?")
    x = input("Type 'y' if you wish to encrypt, type 'n' to decrypt")

    if x == "y":
        print("Do you want to use a data.txt file?")
        y = input("(y/n)")
        if y == "y":
            Encrypting(1)
        elif y =="n":
            Encrypting(0)
        else:
            print("Exiting")
    elif x == "n":
        Decoding()
    else:
        print("Exiting")

Main()
