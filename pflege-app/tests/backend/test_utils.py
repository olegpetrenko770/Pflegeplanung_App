import json

def load_json_from_file(file_path):
    """
    Load JSON data from a file and return it as a dictionary.
    
    :param file_path: Path to the JSON file.
    :return: Dictionary containing JSON data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json_to_file(data, file_path):
    """
    Save a dictionary as JSON data to a file.
    
    :param data: Dictionary to save as JSON.
    :param file_path: Path to the file where JSON data will be saved.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def assert_dicts_equal(dict1, dict2):
    """
    Assert that two dictionaries are equal.
    
    :param dict1: First dictionary.
    :param dict2: Second dictionary.
    :raises AssertionError: If the dictionaries are not equal.
    """
    assert dict1 == dict2, f"Dictionaries are not equal: {dict1} != {dict2}"

def assert_json_files_equal(file_path1, file_path2):
    """
    Assert that the JSON data in two files are equal.
    
    :param file_path1: Path to the first JSON file.
    :param file_path2: Path to the second JSON file.
    :raises AssertionError: If the JSON data in the files are not equal.
    """
    data1 = load_json_from_file(file_path1)
    data2 = load_json_from_file(file_path2)
    assert_dicts_equal(data1, data2)