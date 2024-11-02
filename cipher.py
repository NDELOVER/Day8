def ceaser():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    type =  input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    new_word = []
    if type == "encode":
        for i in text:
            index = alphabet.index(i)
            index += shift
            index %= len(alphabet)
            new_word += alphabet[index]
            encrypted = ''.join(new_word)
        print(f"Here is the encoded result: {encrypted}")
    elif type == "decode":
        for i in text:
            index = alphabet.index(i)
            index -= shift
            index %= len(alphabet)
            new_word += alphabet[index]
            decrypted = ''.join(new_word)
        print(f"Here is the encoded result: {decrypted}")
    else:
        print("You entered the wrong keyword!")


ceaser()
