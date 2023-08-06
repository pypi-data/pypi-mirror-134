import os
import pathlib
import unittest

from tests import TESTS_TLD, RESOURCE_PATH

from sjt.utils import *


class TestUtils(unittest.TestCase):

    def setUp(self) -> None:

        os.chdir(RESOURCE_PATH)

    def test_to_path(self):
        cases = [
            {'path': 'data', 'exists': True},
            {'path': 'templates', 'exists': True},
            {'path': 'nonexistent', 'exists': False},

            {'path': RESOURCE_PATH.joinpath('data'), 'exists': True},
            {'path': RESOURCE_PATH.joinpath('nonexistent'), 'exists': False}
        ]
        for case in cases:
            with self.subTest(msg=case['path']):

                have = to_path(path_str=case['path'])
                print(f"{case['path']} -> {have}")
                if case['exists']:
                    self.assertIsInstance(have, pathlib.Path)
                    self.assertTrue(have.exists())
                else:
                    self.assertEqual(have, None)

if __name__ == '__main__':
    unittest.main()