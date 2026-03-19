x0 = 16441782473165749985269251414928450202051900518929647105868978172963309169080628914206924705003483790602

flag_bytes = x0.to_bytes((x0.bit_length() + 7) // 8, 'big')

# remove any leading null bytes
while flag_bytes[0] == 0:
   flag_bytes = flag_bytes[1:]

flag_text = flag_bytes.decode('utf-8')
print("PLAINTEXT FLAG:", flag_text)

printed flag was: utflag{my_obl1v10u5_fr13nd_ru1n3d_my_c0de}
