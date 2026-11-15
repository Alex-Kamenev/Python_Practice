import unittest

from HasDuplicates import hasDuplicates


class CollidingValue:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return isinstance(other, CollidingValue) and self.value == other.value


class DuplicateTests(unittest.TestCase):
    def test_empty_and_single_none(self):
        self.assertFalse(hasDuplicates([]))
        self.assertFalse(hasDuplicates([None]))

    def test_duplicate_none_and_integers(self):
        self.assertTrue(hasDuplicates([None, None]))
        self.assertTrue(hasDuplicates([1, 2, 1]))

    def test_hash_collisions_do_not_hide_a_duplicate(self):
        self.assertTrue(hasDuplicates([CollidingValue(1), CollidingValue(2), CollidingValue(1)]))
        self.assertFalse(hasDuplicates([CollidingValue(1), CollidingValue(2)]))


if __name__ == '__main__':
    unittest.main()
