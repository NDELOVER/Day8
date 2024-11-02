def ceaser(text,shift,encode_or_decode):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    new_word = ""
    keep_running = True
    while keep_running:
        if encode_or_decode == "decode":
            shift *= -1
        for i in text:
            if i in alphabet:
                index = alphabet.index(i)
                index += shift
                index %= len(alphabet)
                new_word += alphabet[index]
            else:
                new_word+=i
        print(f"Here is the {cipher_type}d result: {new_word}")

        re_run = input("Do you want to rerun? Yes/No:\n").lower()
        if re_run == "no":
            keep_running = False
        else:
            new_word=""
            encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
            text = input("Type your message: ").lower()
            shift = int(input("Type the shift number: "))


cipher_type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))
ceaser(text,shift,cipher_type)
