#!/usr/bin/env python
import subprocess
import sys
import os

# decode a byte object to a string using the UTF-8 format
to_utf8 = lambda x: x.decode('UTF-8')


def Get_Command_Output(command):
    os.environ['PYTHONUNBUFFERED'] = "1"
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            )
    stdout, stderr = proc.communicate()
    stdout = to_utf8(stdout)
    stderr = to_utf8(stderr)
    return stdout, stderr


def Get_Subprocess_Output(cmd, args):
    x_command = Run_Command(cmd, args)
    captured_output = x_command[1]
    return f'The executed command -> {[cmd,args]}\nThe returned output -> {captured_output}'


class Command:
    list_of_commands = []

    def __init__(self, command_list):
        self.list_of_commands = command_list

    @classmethod
    def Run_Command(cls, cmd, args):
        os.environ['PYTHONUNBUFFERED'] = "1"
        proc = subprocess.Popen([cmd],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                )
        stdout, stderr = proc.communicate()
        return proc.returncode, stdout, stderr

    @classmethod
    def Run_Command_No_Args(cls, cmd):
        os.environ['PYTHONUNBUFFERED'] = "1"
        proc = subprocess.Popen([cmd],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                )
        stdout, stderr = proc.communicate()
        return proc.returncode, stdout, stderr


commands = [['ls', '-l'], ['ifconfig']]


x_comms = Command(commands)

for command in commands:
    if(len(command) == 2):
        print(Command.Run_Command(command[0], command[1]))
    else:
        print(Command.Run_Command_No_Args(command[0]))

# ls = subprocess.run(['ps', 'aux'], capture_output=True,
#                     text=True).stdout.strip("\n")
