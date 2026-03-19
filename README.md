# UTCTF 2025 – Cryptography Writeups

## Overview
This repository contains my writeups for cryptography challenges from **UTCTF 2025**.

The goal of these writeups is to document not just the solutions, but the **thought process, vulnerabilities, and cryptographic concepts** behind each challenge.

---

## Challenges Covered

### 1. Fortune Teller (LCG Prediction)
- **Concepts:** Linear Congruential Generators, XOR encryption  
- **Key Idea:** Predicting future outputs of a weak PRNG to recover an encryption key  

### 2. Smooth Criminal (Discrete Log)
- **Concepts:** Modular exponentiation, discrete logarithm problem  
- **Key Idea:** Recovering a secret exponent due to weak cryptographic parameters  

### 3. Oblivious Error (RSA Logic Flaw)
- **Concepts:** RSA, oblivious transfer, implementation vulnerabilities  
- **Key Idea:** Exploiting incorrect use of XOR instead of exponentiation  

---

## Tools & Technologies
- Python  
- `sympy` (discrete logarithms)  
- `Crypto.Util.number` (modular arithmetic)  
- Netcat (`nc`) for interacting with remote services  

---

## Key Takeaways
Across these challenges, I learned:

- Weak random number generators (like LCGs) are predictable  
- Cryptographic security depends heavily on **proper parameter selection**  
- Small implementation mistakes (like using XOR incorrectly) can completely break secure systems  

---

## ⚠️ Disclaimer
These writeups are for **educational purposes only**. All challenges were completed in a legal CTF environment.
