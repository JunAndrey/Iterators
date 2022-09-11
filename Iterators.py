class FlatIterator():
    def __init__(self, list_):
        self.list = list_
        self.index = 0
        self.index_2 = 0

    def __iter__(self):
        self.a = self.list
        return self

    def __next__(self):
        if self.index < len(self.list) and self.index_2 < len(self.list[self.index]):
            x = self.a[self.index][self.index_2]
            self.index_2 += 1
            return x
        elif self.index < len(self.list) and self.index_2 == len(self.list[self.index]):
            self.index += 1
            self.index_2 = 0
            return self.__next__()
        else:
            raise StopIteration


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

for i in FlatIterator(nested_list):
    print(i)

generator = [x for y in nested_list for x in y]
print(generator)


def final_list(list_1):
    for item in list_1:
        if isinstance(item, list):
            yield from final_list(item)
        else:
            yield item


for i in final_list(nested_list):
    print(i)


flat_list = [item for item in final_list(nested_list)]
print(flat_list)

nested_list_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, [11, 12], None],
]


def list_flatten(a):
    list1, list2 = [a], []
    while list1:
        elem = list1.pop()
        if isinstance(elem, list):
            list1.extend(elem)
        else:
            list2.append(elem)
    return list2[::-1]


for i in list_flatten(nested_list_1):
    print(i)
flat_list = [item for item in list_flatten(nested_list_1)]
print(flat_list)
