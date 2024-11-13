def encrypt_message(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():  
            shift_amount = shift % 26 
            new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a')) if char.islower() else \
                       chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted += new_char
        else:
            encrypted += char 
    return encrypted

def decrypt_message(encrypted_message, shift):
    return encrypt_message(encrypted_message, -shift)  

def main():
    while True:
        choice = input(""" 
1.encrypt 
2.decrypt 
q.Quit: 
Do you want to:""").lower()
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            encrypted = encrypt_message(message, shift)
            print(f"Encrypted message: {encrypted}")
        elif choice == '2':
            encrypted_message = input("Enter the encrypted message: ")
            shift = int(input("Enter shift value (1-25): "))
            decrypted = decrypt_message(encrypted_message, shift)
            print(f"Decrypted message: {decrypted}")
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose '1', '2', or 'q'.")

if __name__ == "__main__":
    main()