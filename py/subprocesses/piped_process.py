#!/usr/bin/env python
import subprocess


# for shell=False use absolute paths
p = subprocess.Popen("ps aux | grep zsh", shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

output = 'results.out'

p_stdout = p.stdout.read()
p_stderr = p.stderr.read()

decoder = lambda x: x.decode('UTF-8')


with open(output, 'w+') as save:
    save.write(decoder(p_stdout))
