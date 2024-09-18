from collections import Counter

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = len(ALPHABET)

ENGLISH_LETTER_FREQ = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 
    'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 
    'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 
    'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.49, 
    'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07
}

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char in ALPHABET:
            decrypted_text += ALPHABET[(ALPHABET.index(char) - shift) % N]
        else:
            decrypted_text += char
    return decrypted_text

def calculate_letter_frequency(text):
    text = text.upper()
    letter_counts = Counter(char for char in text if char in ALPHABET)
    total_letters = sum(letter_counts.values())
    letter_freq = {char: (count / total_letters * 100) for char, count in letter_counts.items()}
    return letter_freq

def compare_frequencies(text_freq, reference_freq):
    score = 0
    for char in reference_freq:
        score += abs(reference_freq[char] - text_freq.get(char, 0))
    return score

def find_best_shift(ciphertext):
    best_shift = None
    best_score = float('inf')
    best_text = ""
    
    for shift in range(1, N):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        letter_freq = calculate_letter_frequency(decrypted_text)
        score = compare_frequencies(letter_freq, ENGLISH_LETTER_FREQ)
        
        if score < best_score:
            best_score = score
            best_shift = shift
            best_text = decrypted_text
    
    return best_shift, best_text

def main():
    ciphertext = input("Введите шифртекст: ").upper()
    
    best_shift, best_text = find_best_shift(ciphertext)
    
    print(f"Лучший сдвиг: {best_shift}")
    print(f"Расшифрованный текст: {best_text}")

if __name__ == "__main__":
    main()
