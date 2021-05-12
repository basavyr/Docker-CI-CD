#!/usr/bin/env python
import psutil as ps
import re

story = 'logstash --logstash-process'


match = re.search('logstash', story.lower())
match_2 = re.findall('logstash', story.lower())

print(match.group(0))
print(match_2)