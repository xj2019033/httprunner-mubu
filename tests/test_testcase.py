import os
import unittest

from httprunner_mubu.loader import load_yaml
from httprunner_mubu.runner import run_testcase_yml, run_yaml


class TestSingleTestcase(unittest.TestCase):

    def test_loader_single_api(self):
        """ 加载出的用例内容与原始信息一致
        """
        single_testcase_yaml = os.path.join(os.path.dirname(__file__), "api", "get_homepage.yml")
        loaded_json = load_yaml(single_testcase_yaml)
        self.assertIn("request",loaded_json)
        self.assertEqual(loaded_json["request"]["url"],"https://mubu.com/")

    def test_loader_single_yaml(self):
        single_testcase_yaml = os.path.join(os.path.dirname(__file__), "api", "get_homepage.yml")
        result=run_yaml(single_testcase_yaml)
        self.assertEqual(len(result), 1)
        #self.assertIsInstance(result[0], True)

        single_testcase_yaml = os.path.join(os.path.dirname(__file__), "api", "api_login_submit.yml")
        result = run_yaml(single_testcase_yaml)
        self.assertEqual(len(result), 1)
        #self.assertIsInstance(result[0], True)

    def test_run_testcase_yml(self):
        single_api_yml = os.path.join(os.path.dirname(__file__), "testcase", "mubu_login.yml")
        #print(single_api_yml)
        result =run_yaml(single_api_yml)
        self.assertEqual(len(result), 4)