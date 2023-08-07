import json

FILE_LOCATION = "/tmp/link-checker.txt"

with open(FILE_LOCATION) as f:
  link_checker_result = json.load(f)

listOfFailure = link_checker_result['fail_map']

if listOfFailure:
  RealErrors = []
  skipErrors = []
  
  for failureWebSite in listOfFailure:
    for failure in listOfFailure[failureWebSite]:
      errorCode = failure['status'].get(code)
      if not errorCode:
        skipErrors.append(failure)
        continue

      if 400 <= errorCode and 500 > errorCode:
        RealErrors.append(failure)

  print(RealErrors)
  print(skipErrors)
      
