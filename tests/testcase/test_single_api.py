import os
import unittest

from httprunner_mubu.loader import load_yaml
from httprunner_mubu.runner import run_yaml


class TestSingleAPI(unittest.TestCase):
    """加载出的接口请求参数与原始信息一致
    """
    def test_loader_single_api(self):
        single_api_yml=os.path.join(os.path.dirname(__file__),"api","get_homepage.yml")
        load_json=load_yaml(single_api_yml)
        self.assertIn("request", load_json)
        self.assertEqual(load_json["request"]["url"],"https://mubu.com/")

    def test_run_single_yaml(self):
        single_api_yml = os.path.join(os.path.dirname(__file__), "api", "get_homepage.yml")
        result=run_yaml(single_api_yml)
        self.assertEqual(result,True)

        single_api_yml = os.path.join(os.path.dirname(__file__), "api", "get_login.yml")
        result = run_yaml(single_api_yml)
        self.assertEqual(result, True)

    def test_run_single_yaml_with_jsonpath(self):
        single_api_yml = os.path.join(os.path.dirname(__file__), "api", "api_login_submit.yml")
        result = run_yaml(single_api_yml)
        self.assertEqual(result, True)
