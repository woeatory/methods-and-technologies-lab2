import unittest
from main import *


class TestCircularLinkedList(unittest.TestCase):
    def setUp(self):
        self.CLL = CircularLinkedList()

    def valuesTest(self, action=None, lst=CircularLinkedList):
        if action == lst.append:
            self.assertRaises(TypeError, lst.append, 'aa')
            self.assertRaises(TypeError, lst.append, 1)
            self.assertRaises(TypeError, lst.append, 1.0)
            self.assertRaises(TypeError, lst.append, complex(1.0))
            self.assertRaises(TypeError, lst.append, [1, 2, 3])
            self.assertRaises(TypeError, lst.append, (1, 2, 3))
            self.assertRaises(TypeError, lst.append, {1, 2, 3})
            self.assertRaises(TypeError, lst.append, True)

        elif action == lst.insert:
            self.assertRaises(TypeError, lst.insert, 'aa', -1)
            self.assertRaises(ValueError, lst.insert, 'A', -1)
            self.assertRaises(ValueError, lst.insert, 'A', lst.count + 1)

            self.assertRaises(TypeError, lst.insert, 1, 0)
            self.assertRaises(TypeError, lst.insert, 1.0, 0)
            self.assertRaises(TypeError, lst.insert, complex(1.0), 0)
            self.assertRaises(TypeError, lst.insert, [1, 2, 3], 0)
            self.assertRaises(TypeError, lst.insert, (1, 2, 3), 0)
            self.assertRaises(TypeError, lst.insert, {1, 2, 3}, 0)
            self.assertRaises(TypeError, lst.insert, True, 0)

        elif action == lst.delete:
            self.assertRaises(ValueError, lst.delete, -1)
            self.assertRaises(ValueError, lst.delete, lst.count)

        elif action == lst.deleteAll:
            self.assertRaises(TypeError, lst.deleteAll, 'aa')
            self.assertRaises(TypeError, lst.deleteAll, 1)
            self.assertRaises(TypeError, lst.deleteAll, 1.0)
            self.assertRaises(TypeError, lst.deleteAll, complex(1.0))
            self.assertRaises(TypeError, lst.deleteAll, [1, 2, 3])
            self.assertRaises(TypeError, lst.deleteAll, (1, 2, 3), 0)
            self.assertRaises(TypeError, lst.deleteAll, {1, 2, 3})
            self.assertRaises(TypeError, lst.deleteAll, True)

        elif action == lst.get:
            self.assertRaises(ValueError, lst.get, -1)
            self.assertRaises(ValueError, lst.get, lst.count)

        elif action == lst.findFirst:
            self.assertRaises(TypeError, lst.findFirst, 'AA')
            self.assertRaises(TypeError, lst.findFirst, 1)
            self.assertRaises(TypeError, lst.findFirst, 1.0)
            self.assertRaises(TypeError, lst.findFirst, complex(1.0))
            self.assertRaises(TypeError, lst.findFirst, [1, 2, 3])
            self.assertRaises(TypeError, lst.findFirst, (1, 2, 3), 0)
            self.assertRaises(TypeError, lst.findFirst, {1, 2, 3})
            self.assertRaises(TypeError, lst.findFirst, True)

        elif action == lst.findLast:
            self.assertRaises(TypeError, lst.findLast, 'AA')
            self.assertRaises(TypeError, lst.findLast, 1)
            self.assertRaises(TypeError, lst.findLast, 1.0)
            self.assertRaises(TypeError, lst.findLast, complex(1.0))
            self.assertRaises(TypeError, lst.findLast, [1, 2, 3])
            self.assertRaises(TypeError, lst.findLast, (1, 2, 3), 0)
            self.assertRaises(TypeError, lst.findLast, {1, 2, 3})
            self.assertRaises(TypeError, lst.findLast, True)

        elif action == lst.extend:
            self.assertRaises(TypeError, lst.extend, '1')
            self.assertRaises(TypeError, lst.extend, 1)
            self.assertRaises(TypeError, lst.extend, 1.0)
            self.assertRaises(TypeError, lst.extend, complex(1.0))
            self.assertRaises(TypeError, lst.extend, [1, 2, 3])
            self.assertRaises(TypeError, lst.extend, (1, 2, 3), 0)
            self.assertRaises(TypeError, lst.extend, {1, 2, 3})
            self.assertRaises(TypeError, lst.extend, True)

    def test_length(self):
        for i in range(100):
            self.subTest(self.assertEqual(self.CLL.length(), i))
            self.CLL.append('A')

    def test_append(self):
        self.CLL.append('a')
        self.subTest(self.assertIn('a', self.CLL.head.data))
        self.subTest(self.assertEqual(1, self.CLL.count))
        self.valuesTest(self.CLL.append, self.CLL)
        # self.assertRaises(TypeError, self.CLL.append, 1)
        # self.assertRaises(TypeError, self.CLL.append, 1.0)
        # self.assertRaises(TypeError, self.CLL.append, complex(1.0))
        # self.assertRaises(TypeError, self.CLL.append, [1, 2, 3])
        # self.assertRaises(TypeError, self.CLL.append, (1, 2, 3))
        # self.assertRaises(TypeError, self.CLL.append, {1, 2, 3})
        # self.assertRaises(TypeError, self.CLL.append, True)

    def test_insert(self):
        self.CLL.insert('A', 0)
        self.subTest(self.assertEqual('A', self.CLL.get(0)))
        self.CLL.insert('B', 0)

        self.subTest(self.assertEqual('B', self.CLL.get(0)))
        self.subTest(self.assertEqual('A', self.CLL.get(1)))

        self.CLL.insert('C', 1)
        self.CLL.insert('D', 3)

        self.subTest(self.assertEqual('C', self.CLL.get(1)))
        self.subTest(self.assertEqual('D', self.CLL.get(3)))

        self.valuesTest(self.CLL.insert, self.CLL)

    def test_delete(self):
        self.CLL.append('A')
        self.CLL.append('B')

        self.valuesTest(self.CLL.delete, self.CLL)
        self.assertEqual(self.CLL.delete(1), 'B')

    def test_deleteAll(self):
        self.valuesTest(self.CLL.deleteAll, self.CLL)
        self.CLL.append('A')
        self.CLL.append('A')
        self.CLL.append('B')
        self.CLL.deleteAll('A')

        self.assertEqual(self.CLL.head.data, 'B')

    def test_get(self):
        self.CLL.append('A')
        self.CLL.append('C')
        self.valuesTest(self.CLL.get, self.CLL)
        self.assertEqual(self.CLL.get(1), 'C')

    def test_clone(self):
        self.CLL.append('A')
        self.CLL.append('C')
        self.CLL.append('D')

        expList = CircularLinkedList()
        expList.append('A')
        expList.append('C')
        expList.append('D')

        resList = self.CLL.clone()

        testStatus = 0

        expListLastNode = expList.head
        testListLastNode = resList.head

        for i in range(self.CLL.count):
            if testListLastNode.data != expListLastNode.data:
                testStatus = 0
                break
            testListLastNode = testListLastNode.next
            expListLastNode = expListLastNode.next
            testStatus = 1

        self.assertEqual(1, testStatus)

    def test_reverse(self):
        self.assertIsNone(self.CLL.reverse())
        expectedCLL = CircularLinkedList()
        expectedCLL.append('C')
        expectedCLL.append('B')
        expectedCLL.append('A')

        self.CLL.append('A')
        self.CLL.append('B')
        self.CLL.append('C')
        self.CLL.reverse()

        expListLastNode = expectedCLL.head
        testListLastNode = self.CLL.head

        for i in range(self.CLL.count):
            self.subTest(self.assertEqual(expListLastNode.data, testListLastNode.data))
            testListLastNode = testListLastNode.next
            expListLastNode = expListLastNode.next

    def test_findFirst(self):
        self.assertEqual(self.CLL.findFirst('A'), -1)
        self.CLL.append('A')
        self.CLL.append('B')
        self.CLL.append('B')
        self.CLL.append('C')

        self.valuesTest(self.CLL.findFirst, self.CLL)
        self.subTest(self.assertEqual(self.CLL.findFirst('O'), -1))
        self.subTest(self.assertEqual(self.CLL.findFirst('B'), 1))

    def test_findLast(self):
        self.CLL.append('A')
        self.CLL.append('B')
        self.CLL.append('B')
        self.CLL.append('C')

        self.valuesTest(self.CLL.findLast, self.CLL)
        self.subTest(self.assertEqual(self.CLL.findLast('O'), -1))
        self.subTest(self.assertEqual(self.CLL.findLast('B'), 2))

    def test_clear(self):
        self.CLL.append('A')
        self.assertIsNone(self.CLL.clear(), self.CLL.head)

    def test_extend(self):
        expectedCLL = CircularLinkedList()
        expectedCLL.append('A')
        expectedCLL.append('B')
        expectedCLL.append('C')
        expectedCLL.append('D')
        expectedCLL.append('E')

        secList = CircularLinkedList()
        secList.append('D')
        secList.append('E')

        self.CLL.append('A')
        self.CLL.append('B')
        self.CLL.append('C')

        self.valuesTest(self.CLL.extend, self.CLL)
        self.CLL.extend(secList)

        expListLastNode = expectedCLL.head
        testListLastNode = self.CLL.head

        for i in range(self.CLL.count):
            self.subTest(self.assertEqual(testListLastNode.data, expListLastNode.data))
            testListLastNode = testListLastNode.next
            expListLastNode = expListLastNode.next


if __name__ == '__main__':
    unittest.main()