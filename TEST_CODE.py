##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN
Y = Fore.YELLOW

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''
##################################
from PriorityQueueHeap import HeapPriorityQueue
from PriorityQueueBase import PriorityQueueBase


def result(flag):
    if flag:
        return f"{G}PASSED{W}"

    return f"{R}FAILED{W}"


def sample_heap():
    elements = [(4, "C"), (5, "A"), (6, "Z"), (15, "K"), (9, "F"), (7, "Q"),
                (20, "B"), (16, "X"), (25, "J"), (14, "E"), (12, "H"), (11, "S"), (13, "W")]

    HPQ = HeapPriorityQueue()

    for e in elements:
        el = PriorityQueueBase.Element(e[0], e[1])
        HPQ._HeapPriorityQueue__data.append(el)

    return HPQ


def TEST_utility_getters():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Utility Getters{W}\n")

    HPQ = sample_heap()
    print(f"{B}Current Heap Array: {W}{HPQ}")

    print(f"\n{P}~~~ __get_parent() ~~~{W}")

    exp = [None, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    test = True
    for i in range(1, len(HPQ)):
        p = HPQ._HeapPriorityQueue__get_parent(i)
        if exp[i] != p:
            test = False
    print(f"Correct parent index was returned for each element: {result(test)}")

    p = HPQ._HeapPriorityQueue__get_parent(0)
    test = p is None
    print(f"Root element has no parent and returns None: {result(test)}")

    ##################################################
    print(f"\n{P}~~~ __get_left() ~~~{W}")

    exp = [1, 3, 5, 7, 9, 11]
    test = True
    for i in range(len(exp)):
        c = HPQ._HeapPriorityQueue__get_left(i)
        if exp[i] != c:
            test = False
    print(f"Correct left index was returned for each element: {result(test)}")

    test = True
    for i in range(6, 13):
        c = HPQ._HeapPriorityQueue__get_left(i)
        if c is not None:
            test = False
    print(f"Returns None if no left child: {result(test)}")

    ##################################################
    print(f"\n{P}~~~ __get_right() ~~~{W}")

    exp = [2, 4, 6, 8, 10, 12]
    test = True
    for i in range(len(exp)):
        c = HPQ._HeapPriorityQueue__get_right(i)
        if exp[i] != c:
            test = False
    print(f"Correct right index was returned for each element: {result(test)}")

    test = True
    for i in range(6, 13):
        c = HPQ._HeapPriorityQueue__get_right(i)
        if c is not None:
            test = False
    print(f"Returns None if no right child: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_swap():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Swap Elements{W}\n")

    tester = sample_heap()
    HPQ = sample_heap()
    print(f"{B}Current Heap Array: {W}{HPQ}")

    for i in range(0, 12, 2):
        j = i + 1

        print(f"\n{P}~~~ Swapping {i} ({HPQ[i]}) and {j} ({HPQ[j]}) ~~~{W}")

        HPQ._HeapPriorityQueue__swap(i, j)
        print(f"{B}Updated Heap Array: {W}{HPQ}")

        test = HPQ._HeapPriorityQueue__data[i] == tester._HeapPriorityQueue__data[j] and HPQ._HeapPriorityQueue__data[
            j] == tester._HeapPriorityQueue__data[i]
        print(f"Objects at given indexes were successfully swapped: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_upheap():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Upheap{W}\n")

    HPQ = sample_heap()
    print(f"{B}Current Heap Array: {W}{HPQ}")

    print(f"\n{Y}A new Element 2:T will be added to the heap{W}")
    HPQ.add_element(2, "T")

    el = PriorityQueueBase.Element(2, "T")
    test = HPQ[0] == el
    print(f"New element was swapped to correct position (root): {result(test)}")

    print(f"{B}Updated Heap Array: {W}{HPQ}")

    ##################################################

    print(f"\n\n{Y}A new Element 5:Y will be added to the heap{W}")
    HPQ.add_element(5, "Y")

    el = PriorityQueueBase.Element(5, "Y")
    test = HPQ[6] == el
    print(f"New element was swapped to correct position (6): {result(test)}")

    print(f"{B}Updated Heap Array: {W}{HPQ}")

    ##################################################

    HPQ = HeapPriorityQueue()
    print(f"\n\n{B}An empty Heap was created: {W}{HPQ}")

    print(f"\n\n{Y}A new Element 8:H will be added to the heap{W}")
    HPQ.add_element(8, "H")

    el = PriorityQueueBase.Element(8, "H")
    test = HPQ[0] == el
    print(f"New element was swapped to correct position (root): {result(test)}")

    print(f"{B}Updated Heap Array: {W}{HPQ}")

    ##################################################

    print(f"\n\n{Y}Five new elements will be added to the heap{W}")

    k = [9, 54, 5, 7, 32]
    v = "EUKLD"

    for i in range(len(k)):
        HPQ.add_element(k[i], v[i])

    print(f"{B}Updated Heap Array: {W}{HPQ}")

    test = True
    exp = [5, 7, 32, 9, 8, 54]
    for i, el in enumerate(HPQ):
        if el._Element__key != exp[i]:
            test = False

    print(f"All elements upheaped to correct positions: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_downheap():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Downheap{W}\n")

    HPQ = sample_heap()
    print(f"{B}Current Heap Array: {W}{HPQ}")

    print(f"\n{Y}The min key 4:C will be removed from the heap{W}")
    k, v = HPQ.remove_min()

    el = PriorityQueueBase.Element(13, "W")
    test = HPQ[10] == el
    print(f"New element was swapped to correct position (10): {result(test)}")

    print(f"{B}Updated Heap Array: {W}{HPQ}")

    ##################################################

    exp = [5, 6, 7, 9, 11, 12, 13, 14, 15, 16, 20, 25]
    test = True
    for i in range(len(HPQ)):
        k, v = HPQ.remove_min()
        if exp[i] != k:
            print(f'{k}:{v}')
            test = False

    print(f"\nAll elements removed in correct sequence: {result(test)}")

    test = len(HPQ) == 0
    print(f"Heap is empty: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_docs():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    HPQ = HeapPriorityQueue()

    doc = HPQ.add_element.__doc__
    if doc != None:
        print(f"{B}add_element() Documentation:{W} {doc}\n")
    else:
        print(f"{R}add_element() Documentation Missing{W}\n")

    doc = HPQ.remove_min.__doc__
    if doc != None:
        print(f"{B}remove_min() Documentation:{W} {doc}\n")
    else:
        print(f"{R}remove_min() Documentation Missing{W}\n")

    doc = HPQ._HeapPriorityQueue__get_parent.__doc__
    if doc != None:
        print(f"{B}__get_parent() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__get_parent() Documentation Missing{W}\n")

    doc = HPQ._HeapPriorityQueue__get_left.__doc__
    if doc != None:
        print(f"{B}__get_left() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__get_left() Documentation Missing{W}\n")

    doc = HPQ._HeapPriorityQueue__get_right.__doc__
    if doc != None:
        print(f"{B}__get_right() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__get_right() Documentation Missing{W}\n")

    doc = HPQ._HeapPriorityQueue__swap.__doc__
    if doc != None:
        print(f"{B}__swap() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__swap() Documentation Missing{W}\n")

    doc = HPQ._HeapPriorityQueue__upheap.__doc__
    if doc != None:
        print(f"{B}__upheap() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__upheap() Documentation Missing{W}\n")

    doc = HPQ._HeapPriorityQueue__downheap.__doc__
    if doc != None:
        print(f"{B}__downheap() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__downheap() Documentation Missing{W}\n")

    print("~" * 50, "\n\n")