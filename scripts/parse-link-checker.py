import json
import sys
from pathlib import Path

FILE_LOCATION = "/tmp/link-checker.txt"

if not Path(FILE_LOCATION).exists():
  print("# ✅ No Broken Link")
  sys.exit(0)

with open(FILE_LOCATION) as f:
  link_checker_result = json.load(f)

listOfFailure = link_checker_result['fail_map']

if not listOfFailure:
  sys.exit(0)
  print("# ✅ No Broken Link")

RealErrors = []
skipErrors = []

for failureWebSite in listOfFailure:
  for failure in listOfFailure[failureWebSite]:
    errorCode = failure['status'].get('code')
    if not errorCode:
      skipErrors.append(failure)
      continue

    if 400 <= errorCode and 500 > errorCode:
      RealErrors.append(failure)
    else:
      skipErrors.append(failure)

if RealErrors:
  print("# Broken Link")
  for error in RealErrors:
    print(f"* {error['url']}: {error['status']['code']}")

if skipErrors:
  print("# Skippable error Link")
  for error in skipErrors:
    print(f"* {error['url']}: {error['status']['text']}")
      
if RealErrors:
  sys.exit(1)
