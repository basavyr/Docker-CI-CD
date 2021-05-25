#!/usr/bin/env python
import os
import subprocess
import time


utf8 = 'UTF-8'


class Utils:
    """Helper class that creates output files, deals with string encoding/decoding and much more"""

    @staticmethod
    def encode(obj): return bytes(obj, utf8)

    @staticmethod
    def decode(text): return text.decode(utf8)

    @staticmethod
    def create_file(file_name): return f'{file_name}_command_output.dat'

    @staticmethod
    def search_running_process(process): return f'ps aux | grep {process}'

    @staticmethod
    def Return_Error_Tuple():
        """
        Return a safe-mode tuple [output,error] when the command that was executed by Popen could not finish successfully
        """
        return '-1', 'Command could not be executed'

    @staticmethod
    def Make_Shell_Command(command):
        shell_cmd = ['/bin/bash', '-c', str(command)]
        return shell_cmd


class Process:

    @staticmethod
    def Check_Process_Completion(command):
        try:
            assert command.returncode == 0, 'Unexpected error ocurred'
        except AssertionError as err:
            print(f'There was an issue:\n{err}')
            return -1
        else:
            return 1


def RunCommand(command):
    """
    Execute a shell-specific command within a Python method

    Uses the Popen function, from the subprocess module

    """
    debug_mode = True

    shell_mode = False

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
            if(debug_mode):
                print('There was an issue during command execution')
            output, errors = Utils.Return_Error_Tuple()
            print(
                f'Command output/errors:\nSTDOUT: {output}\nSTDERR: {errors}')
        else:
            if(debug_mode):
                print(f'Command {command} can be executed')
            try:
                output, errors = executed_command.communicate(timeout=10)
            except subprocess.TimeoutExpired:
                executed_command.kill()
                output, errors = Utils.Return_Error_Tuple()
                print(
                    f'Command output/errors:\nSTDOUT: {output}\nSTDERR: {errors}')
            except OSError as os_issue:
                print(f'There was an OS-specific issue.\n{os_issue}')
            except Exception as problem:
                print(
                    f'There was an issue while trying to execute the command:\n{problem}')
            else:
                print(f'Return code: {executed_command.returncode}')
                if(Accept_Bytes(output)):
                    print(f'Command output:\n{output}')
                    Save_Output(command_name, output)

    # execute the command outside the interactive shell
    if(non_shell_mode):
        if(debug_mode):
            print('SHELL mode is turned OFF')
        # the command is called within a safe-mode try/except block
        try:
            cmd = command[0]
            print(f'initial command: {cmd}')
            shell_cmd = Utils.Make_Shell_Command(cmd)
            print(f'shell command: {shell_cmd}')
            executed_command_noShell = subprocess.Popen(shell_cmd,
                                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            if(debug_mode):
                print('There was an issue during command execution')
            output, errors = Utils.Return_Error_Tuple()
            print(
                f'Command output/errors:\nSTDOUT: {output}\nSTDERR: {errors}')
        else:
            print(f'Command {command} can be executed')
            try:
                output, errors = executed_command_noShell.communicate(
                    timeout=10)
            except subprocess.TimeoutExpired:
                executed_command_noShell.kill()
                output, errors = Utils.Return_Error_Tuple()
                print(
                    f'Command output/errors:\nSTDOUT: {output}\nSTDERR: {errors}')
            except OSError as os_issue:
                print(f'There was an OS-specific issue.\n{os_issue}')
                print(errors)
            except Exception as problem:
                print(
                    f'There was an issue while trying to execute the command:\n{problem}')
            else:
                print(f'Return code: {executed_command_noShell.returncode}')
                if(Accept_Bytes(output)):
                    print(f'Command output:\n{output}')
                    Save_Output(command_name, output)


def Save_Output(command_name, output):
    filename = Utils.create_file(command_name)
    # decode the output if it is not a string
    if(Accept_Bytes(output) == -1):
        output = Utils.decode(output)
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
    "MD": 'systemd',
    "CLANG": 'clang++'


}

if (__name__ == '__main__'):
    get_process_instances = [
        [Utils.search_running_process(process_list["CLANG"])]]
    for command in get_process_instances:
        RunCommand(command)
