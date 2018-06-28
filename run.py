import os
import requests
url=""

response_dir=r"requests"
request_dir=r"requests"

for file in os.listdir(os.fsencode(request_dir)):
    filename = os.fsdecode(file)
    # if filename.endswith(".asm") or filename.endswith(".py"):
    with open(os.path.join(request_dir, filename)) as f:
        request= f.read()
        print(request)
        # continue
    # else:
        # continue
