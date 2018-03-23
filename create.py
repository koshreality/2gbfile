import random

with open('file.bin', 'wb') as f:
    for i in range(2 ** 10):
        myArr = bytearray(2 ** 21)

        for j in range(2 ** 19):
            a = random.randint(0, 2 ** 31)
            myArr[4*j:4*j+4] = a.to_bytes(4, byteorder='big')

        if i % 10 == 0:
            print(i)

        f.write(myArr)