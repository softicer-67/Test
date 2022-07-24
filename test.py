''' 1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет
    аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы
    обеих реализаций.
'''
from datetime import datetime


def isEven(value):
    return value % 2 == 0


print('''\nИдеальная реализация value % 2, если остаток от деления == 0, то число четное\n''')


def isEven_1(value):
    if value & 1:
        res = False
    else:
        res = True
    return res


value = 1111

start1 = datetime.now()
for i in range(1000000):
    isEven(value)
print(f'1 вариант: {datetime.now() - start1}, Проверка на четность: {value} - {isEven(value)}')

start2 = datetime.now()
for i in range(1000000):
    isEven_1(value)
print(f'2 вариант: {datetime.now() - start2}, Проверка на четность: {value} = {isEven(value)}')

print('''\nПобитовые операции:  value & 1 используется для проверки, если бит 0 value равно 0 или 1.
В чужом коде очень редко видел подобную реализацию. По времени выполнения разницы не увидел ...\n''')


'''2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы 
и минусы каждой реализации.'''

# Первая реализация:


class RingBuffer:
    def __init__(self, size_max):
        self.max = size_max
        self.data = []

    class __Full:
        def append(self, x):
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max

        def get(self):
            return self.data[self.cur:] + self.data[:self.cur]

    def append(self,x):
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            self.__class__ = self.__Full

    def get(self):
        return self.data

# Вторая реализация:


class CircularBuffer(object):
    def __init__(self, size):
        self.index = 0
        self.size = size
        self._data = []

    def record(self, value):
        if len(self._data) == self.size:
            self._data[self.index] = value
        else:
            self._data.append(value)
        self.index = (self.index + 1) % self.size

    def __getitem__(self, key):
        return(self._data[key])

    def __repr__(self):
        return self._data.__repr__() + ' (' + str(len(self._data)) + ' items)'

    def get_all(self):
        return(self._data)


'''3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный 
ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). 
Объяснить почему вы считаете, что функция соответствует заданным критериям.'''

import random


def qsort(arr):
    if arr == []:
        return []
    else:
        pivot = arr[0]
        lesser = qsort([x for x in arr[1:] if x < pivot])
        greater = qsort([x for x in arr[1:] if x >= pivot])
        return lesser + [pivot] + greater


arr = [random.randint(1, 100000) for i in range(1000)]
print(qsort(arr))

print('''\nQuicksort является одним из наиболее распространенных алгоритмов 
сортировки благодаря относительной простоте реализации и эффективной производительности.''')
