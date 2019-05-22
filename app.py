import sys
import argparse

MEMORY_SIZE = 256

def main():
    bf_code = init()
    print("Output")
    interpretation(bf_code)


def interpretation(bf_code):
    memory = [0 for i in range(MEMORY_SIZE)]
    ptr = 0
    idx = 0
    while idx < len(bf_code):
        if bf_code[idx] == "+":
            memory[ptr] += 1
        elif bf_code[idx] == "-":
            memory[ptr] -= 1
        elif bf_code[idx] == ">":
            ptr += 1
        elif bf_code[idx] == "<":
            ptr -= 1
        elif bf_code[idx] == ".":
            print(chr(memory[ptr]), end="")
        elif bf_code[idx] == ",":
            i = sys.stdin.buffer.read(1)
            if i == b"\r" or i == b"\n":
                continue

            memory[ptr] = ord(i)
            # print(i, ord(i))
        elif bf_code[idx] == "[":
            if memory[ptr] == 0:
                count = 1
                while count != 0:
                    idx += 1
                    if bf_code[idx] == "]":
                        count -= 1
                    elif bf_code[idx] == "[":
                        count += 1
        elif bf_code[idx] == "]":
            if memory[ptr] != 0:
                count = 1
                while count != 0:
                    idx -= 1
                    if bf_code[idx] == "[":
                        count -= 1
                    elif bf_code[idx] == "]":
                        count += 1

        idx += 1


def init():
    parser = argparse.ArgumentParser()

    parser.add_argument("bf_code_fliename")

    args = parser.parse_args()

    bf_code = ""
    with open(args.bf_code_fliename, "rt") as f:
        bf_code = f.read()

    print("Input ({})".format(args.bf_code_fliename))
    print(bf_code)

    return bf_code


if __name__ == "__main__":
    main()
