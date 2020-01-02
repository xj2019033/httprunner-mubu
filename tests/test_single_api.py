import os
import unittest

from httprunner_mubu.loader import load_yaml
from httprunner_mubu.runner import run_api_yaml, run_yaml


class TestSingleAPI(unittest.TestCase):
    """加载出的接口请求参数与原始信息一致
    """
    def test_loader_single_api(self):
        single_testcase_yaml = os.path.join(os.path.dirname(__file__), "api", "get_homepage.yml")
        loaded_json = load_yaml(single_testcase_yaml)
        self.assertIn("request", loaded_json)
        self.assertEqual(loaded_json["request"]["url"], "https://mubu.com/")

    def test_run_single_yaml(self):
        single_testcase_yaml = os.path.join(os.path.dirname(__file__), "api", "get_homepage.yml")
        result = run_yaml(single_testcase_yaml)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], True)

        single_testcase_yaml = os.path.join(os.path.dirname(__file__), "api", "api_login_submit.yml")
        result = run_yaml(single_testcase_yaml)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], True)

    def test_run_single_yaml_with_jsonpath(self):
        single_testcase_yaml = os.path.join(os.path.dirname(__file__), "api", "api_login_submit.yml")
        result = run_yaml(single_testcase_yaml)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], True)
