enc=open("enc").read()
res=''
for c in enc:
    res += hex(ord(c)).lstrip("0x")
print(res)
ascii_str = bytes.fromhex(res).decode('ascii')
print(ascii_str)
