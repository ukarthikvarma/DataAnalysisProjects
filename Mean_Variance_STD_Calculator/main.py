# This entrypoint file to be used in development. Start by reading README.md
from calculation import calculate
from unittest import main

results = calculate([0,1,2,3,4,5,6,7,8])

for key,value in results.items():
  print('{} : {}'.format(key,value))

main(module='test_calculation', exit=False)