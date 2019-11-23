#Create three TestCase classes that test the functionality of all methods in the ListManipulator class

#Import unittest
import unittest
class ListManipulator:
    def __init__(self, list):
        self.list = list

    def min(self):
        if len(self.list) == 0:
            return None

        min = self.list[0]
        for item in self.list:
            if item < min:
                min = item
        return min

    def max(self):
        if len(self.list) == 0:
            return None

        max = self.list[0]
        for item in self.list:
            if item > max:
                max = item
        return max

    def remove(self, value):
        to_remove = []
        for i, item in enumerate(self.list):
            if item == value:
                to_remove.append(i)

        for index in to_remove:
            self.list.pop(index)
        #Return the new list
        return self.list
class TestListManipulator(unittest.TestCase):
    def test_min(self):
        #Create list values
        list = [1, 2, 3, 4, 5]
        check = ListManipulator(list)
        check = check.min()
        self.assertEqual(check, 1)
    def test_max(self):
        list = [1, 2, 3, 4, 5]
        check = ListManipulator(list)
        check = check.max()
        self.assertEqual(check, 5)
    def test_remove(self):
        list = [1, 2, 3, 4, 5]
        new_list = ListManipulator(list)
        new_list = new_list.remove(3)
        self.assertEqual(new_list, [1, 2, 4, 5])
