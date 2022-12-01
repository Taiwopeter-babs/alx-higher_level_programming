#!/usr/bin/python3
import hidden_4
import marshal
import dis


if __name__ == "__main__":

    # disassemble .pyc file
    with open("./hidden_4.pyc", 'rb') as f:
        code = marshal.loads(f.read()[16:])

    # print from second item
    for idx in range(1, len(code.co_names)):
        print(code.co_names[idx])
