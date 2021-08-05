import json
import sys

from parser import Parser
from messages import DEEP_1_0

data = 'test_data'

with Parser(data, DEEP_1_0) as reader:
    for message in reader:
        message = str(message)
        print(type(message))
        print(message)
        text = json.loads(message)
        print(text, file=writer)
