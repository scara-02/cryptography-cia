# Cryptography-CIA

## Prompts

## 1. Workflow Verification
**User Query:** My workflow is as follows: 
1. Plain text is converted to cipher text using the Multiplicative Cipher encryption formula.
2. A hash function is applied to this cipher text to generate a hash value.
3. The hash value is appended to the cipher text and transmitted.
4. The receiver splits the hash from the cipher text.
5. The receiver runs the same hash function on the received cipher text.
6. If the generated hash matches the received hash, the message is deemed uncorrupted. 
**Is this correct?**

## 2. Recommended Hash Functions
Depending on your security needs, you can use:
* **Cryptographic Hashes:** SHA-256 or SHA-3 (Very secure, standard for sensitive data).
* **Non-Cryptographic Hashes:** MurmurHash or CityHash (Faster, used for hash tables).
* **Legacy Hashes:** MD5 or SHA-1 (Fast, but no longer secure against collisions).

---

## 3. The SHA-256 Algorithm
SHA-256 (Secure Hash Algorithm 256-bit) is a member of the SHA-2 family. It produces a fixed 256-bit (32-byte) signature regardless of the input size.

### Key Characteristics:
* **Deterministic:** The same input always yields the same output.
* **Pre-image Resistance:** It is computationally infeasible to reverse the hash back to the original text.
* **Avalanche Effect:** A small change in input (like changing one bit) results in a completely different hash.

---

## 4. Implementing Easy Hash Functions
If you are looking for an "easy" function for learning purposes rather than high-level security, a **Polynomial Rolling Hash** is a great choice. It is much simpler to code than SHA-256 but effective for basic integrity checks.

---

## 5. Polynomial Rolling Hash: Pseudo-Code
The Polynomial Rolling Hash treats a string as a polynomial where each character is a coefficient.


### Pseudo-Code:
```python
function compute_hash(string s):
    P = 31              # A small prime (use 53 for mixed case)
    M = 10^9 + 7        # A large prime modulus
    hash_value = 0
    p_pow = 1
    
    for character in s:
        # Convert char to integer (a=1, b=2...)
        value = (char - 'a' + 1) 
        hash_value = (hash_value + value * p_pow) % M
        p_pow = (p_pow * P) % M
        
    return hash_value
