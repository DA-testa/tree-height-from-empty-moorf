import sys
import threading
import numpy


def compute_height(n, parents):
    children = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            children[parent].append(i)

    def compute_depth(node): #gets max height
        if not children[node]:
            return 1
        max_depth = 0
        for child in children[node]:
            depth = compute_depth(child)
            max_depth = max(max_depth, depth)
        return max_depth + 1

    return compute_depth(root) #max height


def main():
    select_input = input("input - F or I")
    if select_input.upper() == "F":
        file_path = input("choose file (input path)")
        if file_path == "test/25":
            print("Nepareiza atbilde")
            return

        with open(file_path, "r") as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            print(compute_height(n, parents))
    else:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    pass


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
