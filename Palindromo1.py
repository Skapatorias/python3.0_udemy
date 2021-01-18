def palindrome (word): 
    reversed_letters = []
    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = "".join(reversed_letters)
    
    if reversed_word == word:
        return True

    return False


if __name__ == "__main__":
    word = str(input("Escribe una palabra"))

    result = palindrome(word)

    if result is True:
        print ("La palabra {} sí es un palíndromo".format(word))
        
    else:
        print ("La palabra {} no es un palíndromo".format(word))