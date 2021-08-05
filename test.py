import json
import sys
from datetime import datetime

from iex_parser_test import Parser,DEEP_1_0

stime = datetime.now()
data = 'smaller_test_data'
c = 0
jsons = []
writer = open('test.json','w')
with Parser(data, DEEP_1_0) as reader:
    for message in reader:
        if c % 50000 == 0: print(c,datetime.now())
        for a in message:
            if isinstance(message[a],bytes):
                message[a] = message[a].decode('utf-8')
        jsons.append(message)
        c += 1

writer.write(json.dumps(jsons))
print("---END---")
print(datetime.now()- stime)
