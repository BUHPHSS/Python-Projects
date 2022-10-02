# Christmas Tree Program
# Description: This program will print a Christmas tree
# Author: PunGrumpy

def init():
    step = 5
    start = 0
    leaves = 4
    space = leaves * 4
    stem = leaves
    height = 1

    # Leaf
    for xmas in range(1, leaves + 1):
        for i in range(start, step + 1):
            for j in range(space, i, -1):
                print(" ", end="")
            for k in range(1, i + 1):
                print("* ", end="")
            print()
        start += 3
        step += 3

    # Stem
    for i in range(0, stem + height):
        for j in range(0, stem + 1):
            print("  ", end="")
        for k in range(0, stem):
            print(" * ", end="")
        print()


def main():
    init()


if __name__ == "__main__":
    main()
