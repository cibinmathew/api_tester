import json
import os
import requests

url          = "https://jsonplaceholder.typicode.com/posts/1"
response_dir = r"responses"
request_dir  = r"requests"

def sort_dict(obj):
    if isinstance(obj, dict):
        return sorted((k, sort_dict(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(sort_dict(x) for x in obj)
    else:
        return obj

for file in os.listdir(os.fsencode(request_dir)):
    filename = os.fsdecode(file)
    # if filename.endswith(".asm") or filename.endswith(".py"):
    with open(os.path.join(response_dir, filename)) as f:
        response= json.loads(f.read())
    with open(os.path.join(request_dir, filename)) as f:
        request= f.read()
        # continue
    # else:
        # continue
    resp = json.loads(requests.get(url).text)
    print(resp)
    print(sort_dict(resp.items()))
    if sort_dict(resp.items()) == sort_dict(response.items()):
        # print(request)
        print("{} passed".format(filename))
    else:
        print(sort_dict(response.items()))
        print("{} failed".format(filename))
