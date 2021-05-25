#!/usr/bin/env python
import os
import subprocess
import time


utf8 = 'UTF-8'


def encode(obj): return bytes(obj, utf8)
def decode(text): return text.decode(utf8)
def create_file(file_name): return f'{file_name}_command_output.dat'
def search_running_process(process): return f'ps aux | grep {process}'


def Get_Error():
    return '-1', 'Command could not be executed'


def RunCommand(command):
    """
    Execute a shell-specific command within a Python method

    Uses the Popen function, from the subprocess module

    """
    debug_mode = True

    shell_mode = True

    # cannot run ps command in non-shell mode
    non_shell_mode = True

    # use a static name for the command output file
    command_name = 'cmd_results'

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
                executed_command.kill()
            except OSError as os_issue:
                print(f'There was an OS-specific issue.\n{os_issue}')
            except Exception as problem:
                print(
                    f'There was an issue while trying to execute the command:\n{problem}')
            else:
                print(f'Return code: {executed_command.returncode}')
                if(Accept_Bytes(output)):
                    print(f'Command output:\n{decode(output)}')
                    Save_Output(command_name, output)

    # execute the command outside the interactive shell
    if(non_shell_mode):
        if(debug_mode):
            print('SHELL mode is turned OFF')
        # the command is called within a safe-mode try/except block
        try:
            executed_command_noShell = subprocess.Popen(['/bin/bash', '-c', command[0]],
                                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            print('There was an issue during command execution')
        else:
            print(f'Command {command} can be executed')
            try:
                output, errors = executed_command_noShell.communicate(
                    timeout=10)
            except subprocess.TimeoutExpired:
                executed_command_noShell.kill()
            except OSError as os_issue:
                print(f'There was an OS-specific issue.\n{os_issue}')
                print(errors)
            except Exception as problem:
                print(
                    f'There was an issue while trying to execute the command:\n{problem}')
            else:
                print(f'Return code: {executed_command_noShell.returncode}')
                if(Accept_Bytes(output)):
                    print(f'Command output:\n{decode(output)}')
                    Save_Output(command_name, output)


def Save_Output(command_name, output):
    filename = create_file(command_name)
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


process_list = {
    "BASH": 'bash',
    "PY": 'python',
    "SNAP": 'snapd',
    "MD": 'systemd'
}

if (__name__ == '__main__'):
    get_process_instances = [[search_running_process(process_list["PY"])]]
    for command in get_process_instances:
        RunCommand(command)
