class PriorityQueueBase:

    class Element:

        def __init__(self, key, value):
            self.__key = key
            self.__value =  value

        def __lt__(self, other):
            return self.__key < other.__key

        def __gt__(self, other):
            return self.__key > other.__key

        def __eq__(self, other):
          return self.__key == other.__key and self.__value == other.__value

        def __str__(self):
            return f"{self.__key}:{self.__value}"

        def __repr__(self):
            return str(self)

    def is_empty(self):
        return len(self) == 0
