## Thought Process

The equation:

h = g^x mod p

is a classic discrete logarithm problem. The goal is to recover `x`, given `g`, `h`, and `p`.

In secure systems, solving this should be computationally infeasible. However, in CTF challenges, parameters are often intentionally weak or structured in a way that allows solving.

---

## Solution Strategy

I used the `discrete_log` function from the `sympy` library to compute `x` directly.

Once `x` was recovered, I converted it into bytes to obtain the flag.

---

## Why This Works

The difficulty of the discrete logarithm problem depends heavily on the size and structure of `p`.

In this challenge, the parameters allowed the discrete log to be computed efficiently, effectively breaking the cryptosystem and revealing the secret exponent.
