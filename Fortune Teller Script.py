from Crypto.Util.number import inverse

m = 2**32

x1 = 4176616824
x2 = 2681459949
x3 = 1541137174
x4 = 3272915523

d1 = (x2 - x1) % m
d2 = (x3 - x2) % m

a = (d2 * inverse(d1, m)) % m
c = (x2 - a * x1) % m

x5 = (a * x4 + c) % m
print("a =", a)
print("c =", c)
print("output5 =", x5)

cipher = bytes.fromhex("3cff226828ec3f743bb820352aff1b7021b81b623cff31767ad428672ef6")

key = x5.to_bytes(4, "big")

plaintext = bytes(c ^ key[i % 4] for i, c in enumerate(cipher))

print(plaintext)

flag produced: utflag{pr3d1ct_th3_futur3_lcg}
