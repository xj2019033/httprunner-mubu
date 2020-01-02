import jsonpath
import requests
from requests import sessions

from httprunner_mubu.loader import load_yaml

session = sessions.Session()
session_variables_mapping = {}

def extract_json_field(resp, json_field):
    value = jsonpath.jsonpath(resp.json(), json_field)
    return value[0]

def replace_var(content, variables_mapping):
    # https://mubu.com/list?code=$code
    matched = variable_regex_compile.match(content)
    if not matched:
        return content

    var_name = matched[1]
    value = variables_mapping[var_name]
    replaced_content = content.replace("${}".format(var_name), str(value))
    return replaced_content


def parse_content(content, variables_mapping):

    if isinstance(content, dict):
        parsed_content = {}
        for key, value in content.items():
            parsed_value = parse_content(value, variables_mapping)
            parsed_content[key] = parsed_value

        return parsed_content

    elif isinstance(content, list):
        parsed_content = []
        for item in content:
            parsed_item = parse_content(item, variables_mapping)
            parsed_content.append(parsed_item)

        return parsed_content

    elif isinstance(content, str):
        return replace_var(content, variables_mapping)

    else:
        return content


def run_api(api_info):
    """
    :param api_info:
        {
            "request": {},
            "validate: {}
        }
    :return:
    """
    request = api_info["request"]
    global session_variables_mapping
    parsed_request = parse_content(request, session_variables_mapping)

    method = parsed_request.pop("method")
    url = parsed_request.pop("url")
    resp = session.request(method, url, **parsed_request)

    validator_mapping = api_info["validate"]

    for key in validator_mapping:
        if "$" in key:
            # key = "$.code"
            actual_value = extract_json_field(resp, key)
        else:
            actual_value = getattr(resp, key)  # resp.key

        expected_value = validator_mapping[key]

        assert actual_value == expected_value

def run_yaml(yml_file):
    load_json= load_yaml(yml_file)
    request=load_json["request"]
    method =request.pop("method")
    url = request.pop('url')
    resp = requests.request(method, url, **request)
    validator_mapping = load_json["validate"]
    for key in validator_mapping:
        if "$" in key:
            actual_value =extract_json_field(resp, key)
        else:
            actual_value = getattr(resp, key)
        expected_value = validator_mapping[key]
        assert actual_value == expected_value
    return True
