def encrypt_message(message):
    with open('cask_of_amontillado.txt') as f:
        book = f.read().lower().split()

    cipher_text = ""
    for word in message.split():
        for i in range(len(book)):
            if word.lower() == book[i].lower():
                cipher_text += str(i+1) + " "
                break
        else:
            cipher_text += word + " "
    return cipher_text.strip()


def decrypt_message(encrypted_message):
    with open('cask_of_amontillado.txt') as f:
        book = f.read().lower().split()

    plain_text = ""
    words = encrypted_message.split()
    for word in words:
        if word.isnumeric():
            # convert the number to its corresponding word in the book
            index = int(word) - 1
            plain_text += book[index] + " "
        else:
            plain_text += word + " "
    return plain_text.strip()


message = input("Enter your message: ")
encrypted_message = encrypt_message(message)
print("Your encrypted message is:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message)
print("Your decrypted message is:", decrypted_message)