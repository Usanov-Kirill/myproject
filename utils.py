import json 

def dict_list_to_json(dict_list, filename):
    json_str = json.dumps(dict_list, ensure_ascii=False)
    return json_str

def json_to_dict_list(filename): 
    data = json.loads(filename)
    return data