ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = len(ALPHABET)

def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    plaintext = plaintext.replace(" ", "").upper()
    for char in plaintext:
        if char in ALPHABET:
            encrypted_text += ALPHABET[(ALPHABET.index(char) + shift) % N]
        else:
            encrypted_text += char  
    return encrypted_text

def main():
    plaintext = input("Введите текст для шифрования: ")
    shift = int(input("Введите сдвиг (целое число): "))
    
    encrypted_text = caesar_encrypt(plaintext, shift)
    
    print(f"Зашифрованный текст: {encrypted_text}")

if __name__ == "__main__":
    main()
