import multiprocessing
import os
import time
import math

def leibnitz_Reihe(i):
    erg = pow(-1, i) / (2 * i + 1)
    f = open("ergebnis.txt", "a")
    f.write(str(erg))
    f.write("\n")
    f.close()

if __name__ == "__main__":
    start_time = time.time()
    try:
        os.remove("ergebnis.txt")
    except FileNotFoundError:
        pass
    try:
        process_amount = int(input("How many processes do you want to use? "))
    except ValueError:
        process_amount = 1

    try:
        iterations = int(input("How many iterations do you want to use? "))
    except ValueError:
        iterations = 1

    leibnitz_now = 0
    process_count=0
    processes = []
    print("Please wait, this may take a while")
    while leibnitz_now < iterations:
        for i in range(process_amount):
            p = multiprocessing.Process(target=leibnitz_Reihe, args=(leibnitz_now,))
            processes.append(p)
            leibnitz_now += 1

        for x in processes:
            x.start()
        for x in processes:
            x.join()
        processes = []


    ergebnis = 0.0
    end_time = time.time()
    f = open("ergebnis.txt", "r")
    for line in f:
        ergebnis= float(line) +ergebnis
    f.close()

    print(f"Pi mit {iterations} Iterations lautet: {ergebnis*4}")
    print(f"Pi laut math: {math.pi}")
    ## Compare the results
    print(f"Der Unterschied beträgt: {math.pi-ergebnis*4}")
    print(f"Time needed: {end_time-start_time}s")