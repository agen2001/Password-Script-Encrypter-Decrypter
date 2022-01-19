
def Decrypter(word):

    encrypt_word = []
    
    for i in word:
        if i == '99':
            encrypt_word.append('a')
        elif i == '1':
            encrypt_word.append("b")
        elif i == "2":
            encrypt_word.append("c")
        elif i == "3":
            encrypt_word.append("d")
        elif i == "4":
            encrypt_word.append("e")
        elif i == "!":
            encrypt_word.append("f")
        elif i == "@":
            encrypt_word.append("g")
        elif i == "#":
            encrypt_word.append("h")
        elif i == "$":
            encrypt_word.append("i")
        elif i == "j%":
            encrypt_word.append("j")
        elif i == "^":
            encrypt_word.append("k")
        elif i == "&":
            encrypt_word.append("l")
        elif i == "*":
            encrypt_word.append("m")
        elif i == "(":
            encrypt_word.append("n")
        elif i == ")":
            encrypt_word.append("o")
        elif i == ".":
            encrypt_word.append("p")
        elif i == ",":
            encrypt_word.append("q")
        elif i == "/":
            encrypt_word.append("r")
        elif i == "?":
            encrypt_word.append("s")
        elif i == "|":
            encrypt_word.append("t")
        elif i == "{":
            encrypt_word.append("u")
        elif i == "}":
            encrypt_word.append("v")
        elif i == "+":
            encrypt_word.append("x")
        elif i == "+":
            encrypt_word.append("y")
        elif i == "-":
            encrypt_word.append("z")
        else:
            encrypt_word.append(i)  

    return ''.join(encrypt_word)

print(Decrypter(""))
    