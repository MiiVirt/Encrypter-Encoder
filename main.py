import numpy as np

#TODO Handling if less than 32 or over 126 (loop unicode)
#TODO Error handling for empty input and negative keys
#TODO menu inprovement
#TODO function that converts to unicode/char
#TODO Key value can be anything and will be converted into sum of unicode
def Encrypting():

    data = input("Data")

    #Check if key is int
    while True:
        x = input("Key (number)")
        try:
            key = int(x)
            break
        except ValueError:
            print("Invalid input. Enter a round number as key")

    #Convert data to unicode
    datalist = np.array([ord(character) for character in data])

    #Convert key to integrer
    intkey = int(key)

    #Encryption
    encrypted = datalist - intkey

    #Convert to encrypted data
    encrypted_data = ''.join([chr(element) for element in encrypted])

    #Save the data to a data.txt file
    file_path = "data.txt"
    with open(file_path, 'w') as file:
        file.write(encrypted_data)

    #Debuggind
    #print(data)
    #print(encrypted)

    print(encrypted_data)

def Encoding():

    #data = input("Encrypted data")
    file_path = "data.txt"
    with open(file_path, 'r') as file:
        data = file.read()

    #Check if key is int
    while True:
        x = input("Key (number)")
        try:
            key = int(x)
            break
        except ValueError:
            print("Invalid input. Enter a round number as key")

    #Convert data to unicode
    datalist = np.array([ord(character) for character in data])

    #Convert key to integerer
    intkey = int(key)

    #Encoding
    encoded = datalist + intkey

    #Convert data back to characters
    converted = ''.join([chr(element) for element in encoded])

    print(converted)

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
