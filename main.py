class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = self


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def __repr__(self):
        string = ""

        if self.head is None:
            string += "Circular Linked List Is Empty"
            return string

        string += f"Circular Linked List:\n{self.head.data}"
        temp = self.head.next
        while temp != self.head:
            string += f" -> {temp.data}"
            temp = temp.next
        return string

    def length(self):
        return self.count

    def append(self, element):
        self.insert(element, self.count)

    def insert(self, element, nodeIndex):
        if not isinstance(element, str):
            raise TypeError
        if len(element) > 1:
            raise TypeError('Please, write char')

        if (nodeIndex > self.count) | (nodeIndex < 0):
            raise ValueError(f"Index out of range: {nodeIndex}, size: {self.count}")

        if self.head is None:
            self.head = Node(element)
            self.count += 1
            return

        temp = self.head
        for _ in range(self.count - 1 if nodeIndex - 1 == -1 else nodeIndex - 1):
            temp = temp.next

        afterTemp = temp.next
        temp.next = Node(element)
        temp.next.next = afterTemp
        if nodeIndex == 0:
            self.head = temp.next
        self.count += 1
        return

    def delete(self, nodeIndex):
        if (nodeIndex >= self.count) | (nodeIndex < 0):
            raise ValueError(f"Index out of range: {nodeIndex}, size: {self.count}")

        if self.count == 1:
            self.head = None
            self.count = 0
            return

        before = self.head
        for _ in range(self.count - 1 if nodeIndex - 1 == -1 else nodeIndex - 1):
            before = before.next
        after = before.next.next
        deleted = before.next.data
        before.next = after
        if nodeIndex == 0:
            self.head = after
        self.count -= 1
        return deleted

    def deleteAll(self, element):
        if not isinstance(element, str):
            raise TypeError
        if len(element) > 1:
            raise TypeError('Please, write char')

        lastNode = self.head
        nodeIndex = 0
        while nodeIndex != self.count:
            if lastNode.data == element:
                self.delete(nodeIndex)
                nodeIndex = 0
                lastNode = self.head
            else:
                nodeIndex += 1
                lastNode = lastNode.next

    def get(self, nodeIndex):
        if nodeIndex >= self.count or nodeIndex < 0:
            raise ValueError('Index out of range')

        lastNode = self.head

        index = 0
        while index <= nodeIndex:
            if index == nodeIndex:
                return lastNode.data
            index += 1
            lastNode = lastNode.next

    def clone(self):
        cloneList = CircularLinkedList()
        for j in range(self.count):
            cloneList.insert(self.get(j), j)
        return cloneList

    def reverse(self):
        if self.count <= 1:
            print('error: list is empty')
            return

        lastNode = self.head
        for j in range(int(self.count / 2)):
            lastNodeData = self.get(j)
            revNodeData = self.get(self.count - j - 1)
            for i in range(j):
                lastNode = lastNode.next
            lastNode.data = revNodeData
            lastNode = self.head
            i = 0
            while i < self.count - j - 1:
                lastNode = lastNode.next
                i += 1
            lastNode.data = lastNodeData
            lastNode = self.head

    def clear(self):
        while self.head is not None:
            self.delete(0)

    def findFirst(self, element):
        if not isinstance(element, str):
            raise TypeError
        if len(element) > 1:
            raise TypeError('Please, write char')

        if self.count == 0:
            return -1
        lastNode = self.head
        index = 0
        while index != self.count:
            if lastNode.data == element:
                return index
            index += 1
            lastNode = lastNode.next
        return -1

    def findLast(self, element):
        if not isinstance(element, str):
            raise TypeError
        if len(element) > 1:
            raise TypeError('Please, write char')

        lastFoundIndex = None
        index = 0
        lastNode = self.head
        while index != self.count:
            if lastNode.data == element:
                lastFoundIndex = index
            index += 1
            lastNode = lastNode.next
        if lastFoundIndex is None:
            return -1
        return lastFoundIndex

    def extend(self, inList):
        if not isinstance(inList, CircularLinkedList):
            raise TypeError

        lastNode = inList.head
        for i in range(inList.count):
            self.append(lastNode.data)
            lastNode = lastNode.next


a = CircularLinkedList()
a.append('a')
a.append('c')
a.append('d')
a.append('e')
a.append('e')
a.insert('b', 1)
a.insert('e', 2)
print(a)
print(f'List length: {a.length()}')
a.delete(3)
print(a)
a.deleteAll('e')
print(a)
print(f'Element on index 1: {a.get(1)}')

b = a.clone()
print(f'Cloned list: \n{b}')
a.reverse()
print(f'Reversed list: \n{a}')
a.append('e')
a.insert('e', 0)
print('FindFirst method')
print(a.findFirst('e'))
print('FindLast method')
print(a.findLast('e'))

b = CircularLinkedList()
b.append('E')
b.append('F')
a.extend(b)
print(f'Extended list:\n{a}')
