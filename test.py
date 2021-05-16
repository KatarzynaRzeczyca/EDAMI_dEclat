import unittest
import pandas as pd


from declat import create_diffset_from_data, Diffset, compute_next_level, declat


class TestDiffList(unittest.TestCase):
    def test_create_difflist_from_data(self):
        data = {'col1': [1, 4, 1, 2], 'col2': [2, 2, 2, 5], 'col3': [3, 1, 3, 1]}
        data_frame = pd.DataFrame(data=data)
        prediction = Diffset()
        prediction.keys = [[1], [2], [3], [4], [5]]
        prediction.values = [set(), set(), {1, 3}, {0, 2, 3}, {0, 1, 2}]
        prediction.support = [4, 4, 2, 1, 1]
        result = create_diffset_from_data(data_frame)
        self.assertEqual(result.keys, prediction.keys)
        self.assertEqual(result.values, prediction.values)
        self.assertEqual(result.support, prediction.support)

    def test_compute_next_level(self):
        data = {'col1': [1, 2, 1], 'col2': [2, 3, 3], 'col3': [3, 4, 4]}
        data_frame = pd.DataFrame(data=data)
        diffset = create_diffset_from_data(data_frame)

        prediction = Diffset()
        prediction.keys = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        prediction.values = [{2}, set(), {0}, set(), {0}, {0}]
        prediction.support = [1, 2, 1, 2, 1, 2]

        result = compute_next_level(diffset)
        self.assertEqual(result.keys, prediction.keys)
        self.assertEqual(result.values, prediction.values)
        self.assertEqual(result.support, prediction.support)

    def test_declat(self):
        data = {'col1': [1, 2, 1], 'col2': [2, 3, 3], 'col3': [3, 4, 4]}
        data_frame = pd.DataFrame(data=data)

        prediction = Diffset()
        prediction.keys = [[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3],
                           [1, 3, 4], [2, 3, 4]]
        prediction.values = [{1}, {2}, set(), {0}, {2}, set(), {0}, set(), {0}, {0}, set(), {0}, {0}]
        prediction.support = [2, 2, 3, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1]

        result = declat(data_frame)
        self.assertEqual(result.keys, prediction.keys)
        self.assertEqual(result.values, prediction.values)
        self.assertEqual(result.support, prediction.support)