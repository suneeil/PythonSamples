import json
import jsonpath

file_open = open("userdata.json")
file_content = file_open.read()
loads = json.loads(file_content)

print(file_content)
