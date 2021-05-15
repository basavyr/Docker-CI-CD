#!/usr/bin/env python
from subprocess import Popen, PIPE
import subprocess
process = Popen(['ls', '-la'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
# print(stdout)
text=subprocess.getoutput('echo xx')
print(text)