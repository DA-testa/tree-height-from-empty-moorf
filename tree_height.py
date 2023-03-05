import sys
import threading
import numpy

def compute_height(root, parents):
    children = numpy.where(parents == root)[0]
    if children.size == 0:
        return 0
    return max(compute_height(child, parents) for child in children) + 1

def main():
    root = -1
    select_input = input("input - F or I")
    if select_input.upper() == "F":
        file_path = input("choose file (input path)")
        with open(file_path, "r") as f:
            n = int(f.readline())
            parents = numpy.array(f.readline().split(), dtype=numpy.int32)
            print(compute_height(root, parents))
    else:
        n = int(input())
        parents = numpy.array(f.readline().split(), dtype=numpy.int32)
        print(compute_height(root, parents))
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()
