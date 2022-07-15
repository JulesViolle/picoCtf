from Crypto.Util.number import long_to_bytes

from pwn import * # pip install pwntools

conn=connect('jupiter.challenges.picoctf.org',45864)


c=int(conn.recvuntil(b'\n').decode().strip()[2:])
n=int(conn.recvuntil(b'\n').decode().strip()[2:])
e=int(conn.recvuntil(b'\n').decode().strip()[2:])

for i in range(10000000):
    m=pow(c,i,n)
    if b'pic' in long_to_bytes(m):
        print(long_to_bytes(m))
        break
