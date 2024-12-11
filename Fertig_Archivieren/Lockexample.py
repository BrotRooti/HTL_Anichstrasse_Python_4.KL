import multiprocessing

def increment_counter(lock, counter):
    for _ in range(1000):
        #with lock:
        counter.value += 1

if __name__ == "__main__":
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    processes = []

    for _ in range(5):
        p = multiprocessing.Process(target=increment_counter, args=(lock, counter))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Final counter value (with lock): {counter.value}")