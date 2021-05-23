#!/usr/bin/env python
import os
import subprocess
import time


utf8 = 'UTF-8'


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

    # the command should stop after the try/except block
    # check_finish = executed_command.poll()
    # return_code = executed_command.returncode
    # print(f'Finished status: {check_finish}\nReturn code: {return_code}')
    Check_Command_Status(executed_command)

    return output, errors


def Check_Command_Status(command):
    if(command.returncode == 0):
        print(f'The command has been executed successfully')
    else:
        print('There was an issue running the command')


listed_command = "dmesg --help"
string_command = "ls -la"

RunCommand(listed_command)
# print(RunCommand(string_command)[0].decode(utf8))
