import json


def format_json(json_string):
    try:
        json_obj = json.loads(json_string)
        formatted_json = json.dumps(json_obj, indent=4)
        return formatted_json
    except json.decoder.JSONDecodeError as e:
        return f"Error: {e}"


def is_valid_json(json_string):
    try:
        json.loads(json_string)
        return True, None
    except json.decoder.JSONDecodeError as e:
        return False, e
