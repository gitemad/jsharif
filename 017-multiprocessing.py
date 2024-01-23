import time
import multiprocessing

def recur_fibo(n):
    if n <= 1:
        return n
    
    return recur_fibo(n - 1) + recur_fibo(n - 2)

def print_fibo_sequence(n):
    for i in range(n + 1):
        print(recur_fibo(i))


# if __name__ == '__main__':
    # t0 = time.perf_counter()
    # num_processes = multiprocessing.cpu_count()

    # for i in range(num_processes):
    #     print_fibo_sequence(30)
    
    # t1 = time.perf_counter()

    # print(t1 - t0)
        
# if __name__ == '__main__':
#     t0 = time.perf_counter()
#     num_processes = multiprocessing.cpu_count()
#     processes = []

#     for i in range(num_processes):
#         process = multiprocessing.Process(target=print_fibo_sequence, args=(30,))
#         processes.append(process)
    
#     for process in processes:
#         process.start()
    
#     for process in processes:
#         process.join()
    
#     t1 = time.perf_counter()

#     print(t1 - t0)


if __name__ == '__main__':
    t0 = time.perf_counter()
    numbers = range(1, 34)
    pool = multiprocessing.Pool()
    pool.map(print_fibo_sequence, numbers)

    pool.close()
    pool.join()

    t1 = time.perf_counter()

    print(t1 - t0)


# import multiprocessing
# import time

# def add_100(number, lock):
#     for _ in range(100):
#         time.sleep(0.01)
#         with lock:
#             number.value += 1
#         # lock.acquire()
#         # number.value += 1
#         # lock.release()

# if __name__ == '__main__':
#     lock = multiprocessing.Lock()
#     shared_value = multiprocessing.Value('i', 0)
#     print(f'Value at beginning: {shared_value.value}')

#     p1 = multiprocessing.Process(target=add_100, args=(shared_value, lock))
#     p2 = multiprocessing.Process(target=add_100, args=(shared_value, lock))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print(f'Value at end: {shared_value.value}')