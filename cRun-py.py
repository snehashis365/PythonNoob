#!/usr/bin/python3
import sys
import os
import platform
COMPILE=True


def compile(file_name):
    if os.path.exists(file_name[:-2]+".out"):
        print("Re-", end="")
    print(f"Compiling->{file_name}")
    return os.system("cc "+file_name+" -o "+file_name[:-2]+".out -lm")

def run(file_name):
    return_code=0
    if not os.path.exists(file_name[:-2]+".out") or COMPILE:
        return_code=compile(file_name)
    if return_code == 0:
        os.system("./"+file_name[:-2]+".out")
    else:
        print("Compile error!")

def main():
    count=int(0)
    for arg in sys.argv:
        if count == 0:
            pass
        else:
            run(arg)
        count+=1

if __name__ == "__main__":
    main()
