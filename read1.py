import datetime
import time

min_int = 2 ** 31
max_int = 0
sum_int = 0

start_time = time.time()

with open('file.bin', 'rb') as f:

    for i in range(2 ** 9):
        b = f.read(2 ** 22)
        bb = bytearray(b)

        for j in range(2 ** 20):
            a = int.from_bytes(bb[4*j:4*j+4], byteorder='big', signed=False)
            if a > max_int:
                max_int = a
            if a < min_int:
                min_int = a
            sum_int += a

        b = f.read(2 ** 22)

        print(i)
        print('min: ', min_int)
        print('max: ', max_int)
        print('sum: ', sum_int)

print('min: ', min_int)
print('max: ', max_int)
print('sum: ', sum_int)

end_time = time.time()

uptime = end_time - start_time

human_uptime = str(datetime.timedelta(seconds=int(uptime)))

print(human_uptime)
