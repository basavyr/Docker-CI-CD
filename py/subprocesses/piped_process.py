#!/usr/bin/env python
import subprocess
p = subprocess.Popen("ps aux | grep zsh", shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
# for shell=False use absolute paths
p_stdout = p.stdout.read()
p_stderr = p.stderr.read()
print(p_stdout.decode('UTF-8'))
