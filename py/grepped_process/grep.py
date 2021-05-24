#!/usr/bin/env python
import os
import subprocess
import time


utf8 = 'UTF-8'

decode = lambda text: text.decode(utf8)
file = lambda file_name: f'{file_name}_command_output.dat'


def RunCommand(command):
    executed_command = subprocess.Popen(command, shell=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        command_output, command_errors = executed_command.communicate(
            timeout=3)
    except subprocess.TimeoutExpired:
        executed_command.kill()
        command_output, command_errors = executed_command.communicate()
    except OSError as error:
        print(f'There was an issue with running the command.\n{error}')

    command_name = command[0]
    Save_Output(command_name, command_output)

    return command_output, command_errors


def Save_Output(command_name, output):
    filename = file(command_name)
    # decode the output if it is not a string
    if(Accept_Bytes(output) == -1):
        output = decode(output)
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


def Accept_Bytes(input):
    try:
        assert type(input) == bytes, 'The input object is not bytes'
    except AssertionError:
        return 1
    return -1


# listed_command = ["ifconfig", "-h"]
listed_command = ["ls", "-l"]

if (__name__ == '__main__'):
    # RunCommand(listed_command)
    print(Accept_Bytes(b'sss'))
