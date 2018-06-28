import json
import os
import requests
url="https://jsonplaceholder.typicode.com/posts/1"

response_dir=r"requests"
request_dir=r"requests"

def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

for file in os.listdir(os.fsencode(request_dir)):
    filename = os.fsdecode(file)
    # if filename.endswith(".asm") or filename.endswith(".py"):
    with open(os.path.join(response_dir, filename)) as f:
        response= json.loads(f.read())
    with open(os.path.join(request_dir, filename)) as f:
        request= f.read()
        print(request)
        # continue
    # else:
        # continue
    resp = json.loads(requests.get(url).text)
    if ordered(resp.items()) == ordered(response.items()):
        print("passed")
    else:
        print("Faliled")
