import threading
import mmap
import datetime
import time

N = 4
max_ints = [None] * N
min_ints = [None] * N
sum_ints = [None] * N


def foo(n, thread_num):
    min_int = 2 ** 31
    max_int = 0
    sum_int = 0

    with open('file.bin', 'rb') as f:
        fm = mmap.mmap(f.fileno(), length=(2 ** 31)//N, offset=thread_num*(2 ** 31)//N, access=mmap.ACCESS_READ)
        for i in range((2 ** 9) // N):
            b = fm.read(2 ** 22)
            bb = bytearray(b)
            print(thread_num, ' ', i)
            for j in range(2 ** 20):
                a = int.from_bytes(bb[4*j:4*j+4], byteorder='big', signed=False)
                if a > max_int:
                    max_int = a
                if a < min_int:
                    min_int = a
                sum_int += a
            b = f.read(2 ** 22)

    res = [min_int, max_int, sum_int]
    min_ints[thread_num] = min_int
    max_ints[thread_num] = max_int
    sum_ints[thread_num] = sum_int

    print('Thread {}: {}\n'.format(thread_num, res))


start_time = time.time()

threads = [None] * N
for i in range(N):
    threads[i] = threading.Thread(target=foo, args=(N, i))
for i in range(N):
    threads[i].start()
for i in range(N):
    threads[i].join()

print('min: ', min(min_ints))
print('max: ', max(max_ints))
print('sum: ', sum(sum_ints))

end_time = time.time()

uptime = end_time - start_time

human_uptime = str(datetime.timedelta(seconds=int(uptime)))

print(human_uptime)
