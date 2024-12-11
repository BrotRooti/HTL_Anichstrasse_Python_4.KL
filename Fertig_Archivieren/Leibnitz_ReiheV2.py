import multiprocessing
import os
import time
import math


def process_func(leibnitz_start, leibnitz_end, process_id):
    f = open(f"ergebnis{process_id}.txt", "a")
    erg=[]
    for k in range (leibnitz_start, leibnitz_end):
        erg.append(pow(-1, k) / (2 * k + 1))
    for line in erg:
        f.write(str(line))
        f.write("\n")
    f.close()

if __name__ == "__main__":

    try:
        process_amount = int(input("How many processes do you want to use? "))
    except ValueError:
        process_amount = 1

    for process_id in range(process_amount):
        try:
            os.remove(f"ergebnis{process_id}.txt")
        except FileNotFoundError:
            pass
    try:
        iterations = int(input("How many iterations do you want to use? "))
    except ValueError:
        iterations = 1


    processes = []
    chunk_size = iterations // process_amount

    for process_id in range(process_amount):
        leibnitz_start = process_id * chunk_size
        leibnitz_end = (process_id + 1) * chunk_size
        #print(f"Process {process_id} will calculate from {leibnitz_start} to {leibnitz_end}")
        p = multiprocessing.Process(target=process_func, args=(leibnitz_start, leibnitz_end, process_id))
        processes.append(p)

    start_time = time.time()
    for x in processes:
        x.start()
    print("Please wait, this may take a while")
    for x in processes:
        x.join()


    ergebnis = 0.0
    end_time = time.time()
    for process_id in range(process_amount):
        f = open(f"ergebnis{process_id}.txt", "r")
        for line in f:
            ergebnis= float(line) +ergebnis
        f.close()

    print(f"Pi mit {iterations} Iterations lautet: {ergebnis*4}")
    print(f"Pi laut math: {math.pi}")
    ## Compare the results
    print(f"Der Unterschied beträgt: {math.pi-ergebnis*4}")
    print(f"Time needed: {end_time-start_time}s")