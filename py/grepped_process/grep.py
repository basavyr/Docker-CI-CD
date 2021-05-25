#!/usr/bin/env python
import os
import subprocess
import time


utf8 = 'UTF-8'


def encode(obj): return bytes(obj, utf8)
def decode(text): return text.decode(utf8)
def file(file_name): return f'{file_name}_command_output.dat'


def Get_Error():
    return '-1', 'Command could not be executed'


def RunCommand(command):
    """
    Execute a shell-specific command within a Python method

    Uses the Popen function, from the subprocess module

    """
    debug_mode = True

    shell_mode = True
    non_shell_mode = False

    # execute the command with shell mode turned on: that means the command is executed within the interactive shell
    if(shell_mode):
        if(debug_mode):
            print('SHELL mode is turned ON')
        # execute the shell command in safe-mode using the try/except block
        try:
            executed_command = subprocess.Popen(command, shell=True,
                                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            print('There was an issue during command execution')
        else:
            print(f'Command {command} can be executed')
            try:
                output, errors = executed_command.communicate(timeout=10)
            except subprocess.TimeoutExpired:
                print(
                    'The command can be executed and communication protocol can be called')
            except Exception as problem:
                print(
                    f'There was an issue while trying to execute the command:\n{problem}')
            else:
                print(f'Return code: {executed_command.returncode}')

    # execute the command outside the interactive shell
    if(non_shell_mode):
        if(debug_mode):
            print('SHELL mode is turned OFF')
        # the command is called within a safe-mode try/except block
        try:
            executed_command_noShell = subprocess.Popen(command,
                                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            print('There was an issue during command execution')
        else:
            print(f'Command {command} can be executed')
            try:
                output, errors = executed_command_noShell.communicate(
                    timeout=10)
            except subprocess.TimeoutExpired:
                print(
                    'The command can be executed and communication protocol can be called')
            except Exception as problem:
                print(
                    f'There was an issue while trying to execute the command:\n{problem}')
            else:
                print(f'Return code: {executed_command_noShell.returncode}')

    # try:
    #     if(debug_mode):
    #         print('in try')
    #     command_output, command_errors = executed_command_noShell.communicate(
    #         timeout=10)
    # except FileNotFoundError as error:
    #     print('no good')
    # except subprocess.TimeoutExpired:
    #     if(debug_mode):
    #         print('in timeout except')
    #     executed_command_noShell.kill()
    #     command_output, command_errors = Get_Error()
    # except OSError as error:
    #     if(debug_mode):
    #         print('in oserror except')
    #     command_output, command_errors = Get_Error()
    #     print(f'There was an issue with running the command.\n{error}')

    # command_name = command[0]
    # Save_Output(command_name, command_output)

    # if(debug_mode):
    #     print(command_output)

    # return command_output, command_errors


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


if (__name__ == '__main__'):
    command_list = [['docker', '-v'], ['uname', '-a'],
                    ['ls', '-la'], ['df', '-h'], ['tree', '-h']]
    for command in command_list:
        RunCommand(command)
