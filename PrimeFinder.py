import os

cwd = os.getcwd()
files = cwd + "\Files"

def isPrime(N):
    for number in range(2, N):
        if not N % number:
            return False
    return True

def FindPrime(num):
    if isPrime(num):
        print(num, "IS A PRIME NUMBER")
        with open(files + "\PrimesFound.txt", "a") as f2:
            f2.write(str(num) + "\n")
            
with open(files + "\CurrentNumber.txt", "r") as f:
    CurrentNum = int(f.read())


while True:
    FindPrime(int(CurrentNum))
    CurrentNum += 1

    with open(files + "\CurrentNumber.txt", "w") as f:
        f.write(str(CurrentNum))
