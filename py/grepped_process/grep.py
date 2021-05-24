#!/usr/bin/env python
import os
import subprocess
import time


utf8 = 'UTF-8'

file = lambda file_name: f'{file_name}_command_output.dat'


def RunCommand(command):
    executed_command = subprocess.Popen(command, shell=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output, errors = executed_command.communicate(timeout=3)
    except subprocess.TimeoutExpired:
        executed_command.kill()
        output, errors = executed_command.communicate()
    except OSError as error:
        print(f'There was an issue with running the command.\n{error}')

    command_name = command[0]
    Check_Command_Status(executed_command)
    Save_Output(command_name, output)

    return output, errors


def Save_Output(command_name, output):
    filename = file(command_name)
    with open(filename, 'w+') as writer:
        try:
            writer.write(output)
        except TypeError:
            # TODO should implement automatic bytes to string conversion
            writer.write('not good')


def Check_Command_Status(command):
    if(command.returncode == 0):
        print(f'The command has been executed successfully')
        return 1
    else:
        print('There was an issue running the command')
        return -1


listed_command = ["ifconfig", "-h"]

# print(RunCommand(string_command)[0].decode(utf8))
if (__name__ == '__main__'):
    RunCommand(listed_command)
    Save_Output('grep', 'grep')
