#!/usr/bin/env python
import subprocess
import sys
import os

# decode a byte object to a string using the UTF-8 format
to_utf8 = lambda x: x.decode('UTF-8')


class Command:
    list_of_commands = []

    @classmethod
    def Add_Commands(cls, command_list):
        cmd_list = []
        for command in command_list:
            cmd_list.append(command)
        return cmd_list

    def __init__(self, command_list):
        self.list_of_commands = Command.Add_Commands(command_list)

    @classmethod
    def Run_Command(cls, cmd, args):
        os.environ['PYTHONUNBUFFERED'] = "1"
        proc = subprocess.Popen([cmd, args],
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

    @classmethod
    def Get_Command_Output(cls, cmd):
        """output the command result and its errorcode"""
        os.environ['PYTHONUNBUFFERED'] = "1"
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                )
        stdout, stderr = proc.communicate()
        stdout = to_utf8(stdout)
        stderr = to_utf8(stderr)
        return stdout, stderr

    @classmethod
    def Capture_Command_Output(cls, process, args):
        x_command = Command.Run_Command(process, args)
        captured_output = x_command[1]
        return f'The executed command -> {[process,args]}\nThe returned output -> {captured_output}'


commands = [['ls', '-l'], ['ifconfig']]


x_comms = Command(commands)


print(Command.Capture_Command_Output('ls', '-l'))

# for command in x_comms.list_of_commands:
#     if(len(command) == 2):
#         print(Command.Run_Command(command[0], command[1]))
#     else:
#         print(Command.Run_Command_No_Args(command[0]))


# ls = subprocess.run(['ps', 'aux'], capture_output=True,
#                     text=True).stdout.strip("\n")
