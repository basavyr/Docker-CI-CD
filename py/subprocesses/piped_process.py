#!/usr/bin/env python
import subprocess

decoder = lambda x: x.decode('UTF-8')


class Piped_Process:

    def __init__(self, command_list):
        if(len(command_list) == 1):
            self.piped_command = f'{command_list[0]}'
        else:
            self.piped_command = Piped_Process.Generate_Pipe(command_list)

    @classmethod
    def Generate_Pipe(cls, command_list):
        piped_command = f''
        cmd_idx = 0
        for cmd in command_list:
            if(cmd_idx == 0):
                piped_command = cmd
            else:
                piped_command = piped_command + ' | ' + cmd
            cmd_idx += 1
        return piped_command

    @classmethod
    def Run_Process(cls, proc_list):
        """Execute a piped command after each argument has been properly added in the piped instruction
        Returns the output and the error of the executed command
        """

        piped_process = Piped_Process(proc_list).piped_command
        process = subprocess.Popen(piped_process, shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        try:
            process_output = process.stdout.read()
            process_error = process.stderr.read()
        except Exception as exc:
            print(
                f'Issue while running process within the script...\nReason{exc}')
            process.kill()
        return process_output, process_error

    @classmethod
    def Get_Process_Output(cls, proc_list):
        process = subprocess.Popen(proc_list, shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, errors = process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            output, errors = process.communicate()
        return output, errors


command_list = ['ls -la', 'grep  dat']

piped = Piped_Process.Get_Process_Output(command_list)
if(piped[1] != b''):
    print('😭')
    print(piped)
else:
    print('🥰')
    print(piped)
