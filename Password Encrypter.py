
def Encrypt(word):

    encrypt_word = []
    
    for i in word:
        if i == 'a':
            encrypt_word.append('99')
        elif i == 'b':
            encrypt_word.append("1")
        elif i == "c":
            encrypt_word.append("2")
        elif i == "d":
            encrypt_word.append("3")
        elif i == "e":
            encrypt_word.append("4")
        elif i == "f":
            encrypt_word.append("!")
        elif i == "g":
            encrypt_word.append("@")
        elif i == "h":
            encrypt_word.append("#")
        elif i == "i":
            encrypt_word.append("$")
        elif i == "j":
            encrypt_word.append("%")
        elif i == "k":
            encrypt_word.append("^")
        elif i == "l":
            encrypt_word.append("&")
        elif i == "m":
            encrypt_word.append("*")
        elif i == "n":
            encrypt_word.append("(")
        elif i == "o":
            encrypt_word.append(")")
        elif i == "p":
            encrypt_word.append(".")
        elif i == "q":
            encrypt_word.append(",")
        elif i == "r":
            encrypt_word.append("/")
        elif i == "s":
            encrypt_word.append("?")
        elif i == "t":
            encrypt_word.append("|")
        elif i == "u":
            encrypt_word.append("{")
        elif i == "v":
            encrypt_word.append("}")
        elif i == "w":
            encrypt_word.append("+")
        elif i == "x":
            encrypt_word.append("-")
        elif i == "y":
            encrypt_word.append("=")
        elif i == "z":
            encrypt_word.append("_")
        else:
            encrypt_word.append(i)  

    return ''.join(encrypt_word)

print(Encrypt(""))
    