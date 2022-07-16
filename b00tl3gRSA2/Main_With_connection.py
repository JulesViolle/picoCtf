from Crypto.Util.number import long_to_bytes

from pwn import * # pip install pwntools

conn=connect('jupiter.challenges.picoctf.org',45864)


c=int(conn.recvuntil(b'\n').decode().strip()[2:])
n=int(conn.recvuntil(b'\n').decode().strip()[2:])
e=int(conn.recvuntil(b'\n').decode().strip()[2:])

for d in range(10000000):
    m=pow(c,d,n)
    ltb=long_to_bytes(m)
    if b'pic' in ltb:
        print(ltb.decode())
        break
