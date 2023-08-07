import json

FILE_LOCATION = "/tmp/link-checker.txt"

with open(FILE_LOCATION) as f:
  link_checker_result = json.load(f)

listOfFailure = link_checker_result['fail_map']

if listOfFailure:
  RealErrors = {}
  
  
  for failureWebSite in listOfFailure:
    for failure in listOfFailure[failureWebSite]:
      print(failure)
      
