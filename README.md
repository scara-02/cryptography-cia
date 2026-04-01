# Cryptography-CIA

## 1. Workflow
**User Query:** My workflow is as follows: 
1. Plain text is converted to cipher text using the Multiplicative Cipher encryption formula.
2. A hash function is applied to this cipher text to generate a hash value.
3. The hash value is appended to the cipher text and transmitted.
4. The receiver splits the hash from the cipher text.
5. The receiver runs the same hash function on the received cipher text.
6. If the generated hash matches the received hash, the message is deemed uncorrupted. 



## 2. Polynomial Rolling Hash: Pseudo-Code
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
