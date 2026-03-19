## Thought Process

This challenge involved a network service implementing a form of RSA-based oblivious transfer.

After reviewing the provided server code, I noticed something unusual:

v = (x0 + (k ^ e)) % N

Instead of modular exponentiation (`k^e mod N`), the code uses a bitwise XOR (`^`), which is not cryptographically secure.

---

## Solution Strategy

Because XOR is reversible, I leveraged the relationship between `x0` and `x1`:

k = (x1 - x0) ^ e

Submitting this value of `k` to the server produced two messages. Based on the challenge hint, only one of them was valid.

I converted the valid message from an integer into bytes and decoded it to retrieve the flag.

---

## Why This Works

RSA relies on modular exponentiation being a one-way function. Replacing exponentiation with XOR breaks this property completely.

XOR is easily reversible, allowing direct manipulation of values that should otherwise be protected. This flaw made it possible to recover a valid message without needing to break RSA itself.
