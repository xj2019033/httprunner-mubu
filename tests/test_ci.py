import os
import unittest
import subprocess

class TestCli(unittest.TestCase):

    def test_hogrun_single_yaml(self):
        single_api_yml = os.path.join(os.path.dirname(__file__), "api", "get_homepage.yml")
        project_root_dir=os.path.dirname(__file__)
        #subprocess.run("python -m httpruner_mubu.cli {}".format(single_api_yml),cwd=project_root_dir)