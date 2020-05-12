#!/usr/bin/env python
import tika
tika.initVM()
from tika import parser
parsed = parser.from_file('C:\\Users\\sambe\\Projects\\Cover_Letter_Analysis\\Cover_Letters\\samplecoverletter_001')
print(parsed["metadata"])
print(parsed["content"])
