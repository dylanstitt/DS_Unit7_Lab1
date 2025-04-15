# Dylan Stitt
# Unit 7 Lab 1
# Heap

# Implementation & testing of Heap Priority Queue

# Import file
from TEST_CODE import *
import os

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''

def main():

    # TEST 1 - Test utility getters
    # BEFORE TESTING: implement get_parent, get_left, get_right
    TEST_utility_getters()

    # TEST 2 - Test swap utility
    # BEFORE TESTING: implement swap
    TEST_swap()

    # TEST 3 - Test Add element & upheap utility
    # BEFORE TESTING: implement add_element, upheap
    TEST_upheap()

    # TEST 4 - Test remove min & downheap utility
    # BEFORE TESTING: implement remove_min, downheap
    TEST_downheap()
    TEST_docs()

if __name__ == "__main__":
    os.system("cls")
    main()
