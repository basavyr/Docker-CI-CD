#!/usr/bin/env python
import subprocess
import os
import time

# decode bytes to string
def decoder(x): return x.decode('UTF-8')


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
    def Get_Process_Output(cls, piped_process):
        process = subprocess.Popen(piped_process, shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, errors = process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            output, errors = process.communicate()
        return output, errors

    @classmethod
    def Save_Process_Output(cls, full_command, output_file):
        # append the directory name for the relative path of the register
        # dir_output_file = f'{Register.register_directory_name}/{output_file}'

        process = Piped_Process.Get_Process_Output(full_command)
        process_output = process[0]
        process_error = process[1]
        decoded_output = 'x'
        if(process_error == b''):
            return_code = 1
        else:
            return_code = -1
        if(return_code == 1):
            decoded_output = decoder(process_output)
        with open(output_file, 'w+') as saver:
            try:
                saver.write(decoded_output)
            except Exception as err:
                print(f'Could not write to the file...\nReason: {err}')
                return -1

    @classmethod
    def Generate_Command_List(cls, process, command_list):
        grep_process = f'grep {process}'
        new_command_list = list(command_list)
        new_command_list.insert(1, grep_process)
        return new_command_list

    @classmethod
    def Create_Process_Register(cls, process, command_list):
        new_command_list = Piped_Process.Generate_Command_List(
            process, command_list)
        grepped_command = Piped_Process.Generate_Pipe(new_command_list)
        return grepped_command


class Register:

    register_directory_name = 'register'

    @classmethod
    def Create_Register_Directory(cls, register_name):
        try:
            os.mkdir(register_name)
        except FileExistsError as err:
            print(f'Could not make directory.\nReason: {err}')
            return
        return

    @classmethod
    def Create_File_Register(cls, proc_name, command_list):
        file_name = f'{Register.register_directory_name}/{proc_name}.list'
        full_command = Piped_Process.Create_Process_Register(
            proc_name, command_list)
        print(f'Full command: {full_command}')
        with open(file_name, 'w+'):
            try:
                Piped_Process.Save_Process_Output(
                    full_command, file_name)
            except Exception as exc:
                print(f'Error: {exc}')


command = ['ps aux', 'awk \'{print $2,$11,$12}\'']

process_list = ['logstash', 'ssh', 'python', 'bash', 'code']


if(__name__ == '__main__'):
    # creating the directory where each instance of a process will be saved as a file
    Register.Create_Register_Directory(Register.register_directory_name)

    runtime=True
    
    total_execution_time=5
    start_time=time.time()

    while(runtime):
        for proc in process_list:
            Register.Create_File_Register(proc, command)
        if(time.time()-start_time>=total_execution_time):
            runtime=False
        else:
            time.sleep(1)
