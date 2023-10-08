def caesar_encrypt(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            # Apply the Caesar cipher shift
            char_code = ord(char) - start
            encrypted_char = chr((char_code + shift) % 26 + start)
            cipher_text += encrypted_char
        else:
            # If the character is not a letter, keep it unchanged
            cipher_text += char
    return cipher_text

plain_text = input("Enter the plain text: ")
shift = int(input("Enter the Caesar cipher shift (an integer): "))

cipher_text = caesar_encrypt(plain_text, shift)

print("Plain Text: ", plain_text)
print("Cipher Text:", cipher_text)