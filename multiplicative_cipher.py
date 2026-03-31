import math

ALPHABET_SIZE = 26

def mod_inverse(k, m):
    for i in range(1, m):
        if (k * i) % m == 1:
            return i
    raise ValueError(f"No inverse for key {k} mod {m}")
def encrypt(plaintext, key):
    if math.gcd(key, ALPHABET_SIZE) != 1:
        raise ValueError(f"Key {key} is not coprime with {ALPHABET_SIZE}")
    result = []
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr(base + (key * (ord(ch) - base)) % ALPHABET_SIZE))
        else:
            result.append(ch)
    return ''.join(result)
def decrypt(ciphertext, key):
    return encrypt(ciphertext, mod_inverse(key, ALPHABET_SIZE))
def compute_hash(text):
    P = 31
    M = 10**9 + 7
    hash_value = 0
    p_power = 1
    for char in text:
        char_numeric_value = (ord(char) - ord('a') + 1)
        hash_value = (hash_value + (char_numeric_value * p_power)) % M
        p_power = (p_power * P) % M
    return str(hash_value)
def sender(plaintext, key):
    ciphertext = encrypt(plaintext, key)
    hash_value = compute_hash(ciphertext)
    message = ciphertext + "||" + hash_value
    print(f"Plaintext        : {plaintext}")
    print(f"Ciphertext       : {ciphertext}")
    print(f"Hash of cipher   : {hash_value}")
    print(f"Sent message     : {message}")
    return message

def receiver(message, key):
    ciphertext, received_hash = message.split("||")
    computed_hash = compute_hash(ciphertext)
    print(f"\nReceived message : {message}")
    print(f"Ciphertext       : {ciphertext}")
    print(f"Received hash    : {received_hash}")
    print(f"Computed hash    : {computed_hash}")

    if computed_hash == received_hash:
        print("Integrity check  : PASSED (message not corrupted)")
        plaintext = decrypt(ciphertext, key)
        print(f"Decrypted text   : {plaintext}")
    else:
        print("Integrity check  : FAILED (message corrupted!)")

if __name__ == "__main__":
    print("=== SENDER SIDE ===")
    plaintext = input("Enter the plain text you want to encrypt : ")
    key = int(input("Enter the key (must be coprime with 26) : "))
    print(f"Plaintext input  : {plaintext}")
    print(f"Key input        : {key}")
    message = sender(plaintext, key)
    print("\n=== RECEIVER SIDE ===")
    receiver(message, key)
    # simulate tampering
    print("\n=== SIMULATING TAMPERED MESSAGE ===")
    tampered = "X" + message[1:]  # corrupt first character
    receiver(tampered, key)







