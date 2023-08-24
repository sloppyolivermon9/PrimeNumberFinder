from time import sleep
import os

cwd = os.getcwd()
files = cwd + "\Files"

def isPrime(N):
    for number in range(2, N):
        if N % number == 0:
            return False
    return True

def FindPrime(num):
    if isPrime(num) == True:
        print(num, "IS A PRIME NUMBER")
        with open(files + "\PrimesFound.txt", "a") as f2:
            f2.write(str(num) + "\n")
            
f = open(files + "\CurrentNumber.txt", "r")
CurrentNum = int(f.read())
f.close()

while True:
    FindPrime(int(CurrentNum))
    sleep(0.1)
    CurrentNum += 1

    with open(files + "\CurrentNumber.txt", "w") as f:
        f.write(str(CurrentNum))
