# Dylan Stitt
# Unit 7 Lab 1
# Heap

from PriorityQueueBase import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self.__data = []

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        return str(self.__data)

    def __getitem__(self, i):
      return self.__data[i]

    def __iter__(self):
      for el in self.__data:
        yield el

    def add_element(self, key, value):
        """Insert a new element into the heap."""
        ele = self.Element(key, value)
        self.__data.append(ele)
        self.__upheap(len(self.__data)-1)

    def remove_min(self):
        """Remove and return the element with top priority."""
        if len(self) == 0:
            raise ValueError("Heap is empty")

        _tuple = self.__data[0]._Element__key, self.__data[0]._Element__value

        self.__swap(0, len(self.__data)-1)
        del self.__data[-1]
        self.__downheap(0)

        return _tuple

    def __get_parent(self, i):
        """Return the location of the parent of the element at index i."""
        if len(self) == 0:
            return

        ind = (self.__data.index(self.__data[i]) - 1) // 2

        if 0 <= ind < len(self):
            return ind
        return None

    def __get_left(self, i):
        """Return the location of the left child of the element at index i."""
        if len(self) == 0:
            return

        ind = (2*self.__data.index(self.__data[i])) + 1

        if 0 <= ind < len(self):
            return ind
        return None

    def __get_right(self, i):
        """Return the location of the right child of the element at index i."""
        if len(self) == 0:
            return

        ind = (2*self.__data.index(self.__data[i])) + 2

        if 0 <= ind < len(self):
            return ind
        return None

    def __swap(self, ind1, ind2):
        """Swap the values at the given array indexes."""
        if 0 <= ind1 < len(self) and 0 <= ind2 < len(self):
            self.__data[ind1], self.__data[ind2] = self.__data[ind2], self.__data[ind1]

    def __upheap(self, ind):
        """Recursively reorganize the heap array after an insertion."""
        if self.__get_parent(ind) is None:
            return

        if self.__data[self.__get_parent(ind)]._Element__key > self.__data[ind]._Element__key:
            newInd = self.__get_parent(ind)
            self.__swap(ind, self.__get_parent(ind))
            self.__upheap(newInd)

    def __downheap(self, ind):
        """Recursively reorganize the heap array after a deletion."""
        LChild = self.__get_left(ind)
        RChild = self.__get_right(ind)

        if LChild is not None and RChild is not None:
            if self.__data[LChild]._Element__key < self.__data[RChild]._Element__key:
                child = LChild
            else: child = RChild

            self.__swap(ind, child)
            self.__downheap(child)
