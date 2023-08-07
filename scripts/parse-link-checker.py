import json

FILE_LOCATION = "/tmp/link-checker.txt"

with open(FILE_LOCATION, 'w') as f:
  link_checker_result = json.load(f)

print(link_checker_result)
