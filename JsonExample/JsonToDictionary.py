import json

#Parse String to Json
objDict = '{"key1":"val1", "key2":"val2", "key3":"val3"}'

json_result = json.loads(objDict)
print(json_result)

