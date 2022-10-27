def b(given):
    return bin(int.from_bytes(given.encode(),'big'))

def xor(encrypted, key):
    output = ""
    if len(encrypted) == len(key):
        for i in range(0, len(encrypted)):
            if encrypted[i] == "1" and key[i] == "0":
                output = output + "1"
            elif encrypted[i] == "0" and key[i] == "1":
                output = output + "1"
            else:
                output = output + "0"
        print("The decrypted data is:\n" + output)
    else:
        print("The two inputs must be the same length!")
        
def sxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

in1 = "100"
in2 = "101"

xor(b(in1),b(in2))
print(sxor(b(in1),b(in2)))