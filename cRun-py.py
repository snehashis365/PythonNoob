#!/usr/bin/python3
import sys
import os
import platform
import getopt

# Some variables declared are for future use
VERSION = "0.8.15.2"
COMPILE = False
EXECUTE = True
BUILD_MENU = False
SINGLE_FILE = False
DEL_OBJ = False
SHOW_TIME = False

# Color codes
LGREEN = "\033[1;32m"
RED = "\033[0;31m"
BLUE = "\033[0;34m"
LBLUE = "\033[0;36m"
NORMAL = "\033[0m"


def clear():  # Executes command depending on OS
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def banner():  # Builds banner
    print(LBLUE, end="")
    print(r"""
                 ____                __  __
          _____ / __ \ __  __ ____   \ \ \ \
         / ___// /_/ // / / // __ \   \ \ \ \
        / /__ / _, _// /_/ // / / /   / / / /
        \___//_/ |_| \__,_//_/ /_/   /_/ /_/

    """)
    print(f"{LGREEN}                          - by snehashis365{NORMAL}")
    print(f"Version : {LGREEN}{VERSION}(py){NORMAL}")
    print("Re-Compile : ", end="")
    if COMPILE:
        print(f"{BLUE}On{NORMAL}")
    else:
        print(f"{LGREEN}Off{NORMAL}")
    print("Auto Cleanup : ", end="")
    if DEL_OBJ:
        print(f"{RED}On{NORMAL}")
    else:
        print(f"{LGREEN}Off{NORMAL}")
    print("\n")


def compile_c(file_name):
    print(BLUE, end="")  # Setting color prior
    if os.path.exists(file_name[:-2] + ".out"):
        print("Re-", end="")
    print(f"Compiling{NORMAL}->{file_name}\n")
    return os.system("cc " + file_name + " -o " + file_name[:-2] + ".out -lm")


def run(file_name):
    return_code = 0
    if not os.path.exists(file_name[:-2] + ".out") or COMPILE:
        return_code = compile_c(file_name)
    if return_code == 0:
        print(f"{LGREEN}Executing{NORMAL}->{file_name}\n")
        os.system("./" + file_name[:-2] + ".out")
        print(f"\n{LGREEN}Done{NORMAL}\n")
    else:
        print("Compile error!")


def main():
    args = []
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcrmtvdsiu",
                                   ["help", "compile", "run", "menu", "time", "version", "cleanup", "super", "install",
                                    "update"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for opt, a in opts:
        if opt in ["-h", "--help"]:
            print("Help message here")
            sys.exit()
        elif opt in ["-c", "--compile"]:
            COMPILE = True
            EXECUTE = False
        elif opt in ["-r", "--run"]:
            EXECUTE = True
        elif opt in ["-m", "--menu"]:
            BUILD_MENU = True
        elif opt in ["-t", "--time"]:
            SHOW_TIME = True
        elif opt in ["-v", "--version"]:
            print(f"cRun {VERSION}(py) by snehashis365")
            sys.exit()
        elif opt in ["-d", "--cleanup"]:
            DEL_OBJ = True
        elif opt in ["-s", "--super"]:
            print("Attempting sudo")
            os.system(f"sudo {sys.argv[0]}")
            sys.exit()
        elif opt in ["-i", "--install"]:
            print("Call Install function(Coming Soon)")
        elif opt in ["-u", "--update"]:
            print("Call update function(Coming Soon)")
    # End of options handling

    banner()
    count = 0
    err_count = 0
    if len(args) == 2:
        pass
    else:
        for arg in args:
            if EXECUTE:
                run(arg)
            else:
                return_code = compile_c(arg)
                if return_code > 0:
                    err_count += 1
            count += 1
        print(f"Total: {count - 1}\nFailed: {err_count}\nSuccess: {count - err_count - 1}")


if __name__ == "__main__":
    main()
