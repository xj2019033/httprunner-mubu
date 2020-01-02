import os
import unittest

from httprunner_mubu.loader import load_yaml


class TestSingleTestcase(unittest.TestCase):

    def test_loader_single_testcase(self):
        """ 加载出的用例内容与原始信息一致
        """
        single_testcase_yaml = os.path.join(os.path.dirname(__file__), "testcase", "mubu_login.yml")
        loaded_json = load_yaml(single_testcase_yaml)
        self.assertIsInstance(loaded_json, list)
        self.assertEqual(len(loaded_json), 4)