alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+','@','.']


direction = "d"
text = input("Type your encoded message:\n")
shift = 5

def encrypt_decrypt(text, shift):
    newString = list(text)
    increment = 0
    while increment != len(newString):
        if newString[increment] != " ":
            index = alphabet.index(newString[increment])
            if direction[0] == "e" or direction[0] == "E":
                newIndex = index + shift
            else:
                newIndex = index - shift
            if newIndex <= (len(alphabet) - 1):
                newString[increment] = alphabet[newIndex]
            else:
                secondIndex = newIndex - (len(alphabet))
                newString[increment] = alphabet[secondIndex]
        increment+=1
    return listToString(newString)

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

print(encrypt_decrypt(text, shift))


