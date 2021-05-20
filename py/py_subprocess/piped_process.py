#!/usr/bin/env python
import subprocess
import os
import time


# decode bytes to string
def decoder(x): return x.decode('UTF-8')


class Process:

    # the command which will be used for checking if a certain process/service is running on the system or not
    process_getter_command = ['ps aux', 'awk \'{print $2,$11,$12}\'']

    # def __init__(self, command_list):
    #     if(len(command_list) == 1):
    #         self.piped_command = f'{command_list[0]}'
    #     else:
    #         self.piped_command = Process.Generate_Pipe(command_list)

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
    def Run_Process(cls, piped_command):
        """Execute a piped command after each argument has been properly added in the piped instruction
        Returns the output and the error of the executed command
        """
        process = subprocess.Popen(piped_command, shell=True,
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
    def Get_Process_Output(cls, piped_command):
        process = subprocess.Popen(piped_command, shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, errors = process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            output, errors = process.communicate()
        return output, errors

    @classmethod
    def Save_Process_Output(cls, piped_command, output_file):
        # execute the process and retrieve its output from the console
        process = Process.Get_Process_Output(piped_command)

        process_output = process[0]
        process_error = process[1]

        decoded_output = ''
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
    def Generate_Grepped_Command(cls, process, command_list):
        grep_process = f'grep {process}'
        new_command_list = list(command_list)
        new_command_list.insert(1, grep_process)
        return new_command_list

    @classmethod
    def Create_Full_Command(cls, process, command_list):
        new_command_list = Process.Generate_Grepped_Command(
            process, command_list)
        grepped_command = Process.Generate_Pipe(new_command_list)
        return grepped_command

    @classmethod
    def Count_Running_Instances(cls, process):
        """
        Count the number of running instances for a given process
        """
        process_path = f'{Register.register_directory_name}/{process}.list'
        # print(process_path)
        with open(process_path, 'r+') as process_reader:
            lines = process_reader.readlines()
        return len(lines)


class Register:

    register_directory_name = 'register'

    @ classmethod
    def Create_Register_Directory(cls, register_name):
        try:
            os.mkdir(register_name)
        except FileExistsError:
            # print(f'Could not make directory.\nReason: {err}')
            pass
        return

    @ classmethod
    def Create_File_Register(cls, proc_name, command_list):
        debug_moode = 0

        if(debug_moode):
            print('Creating the proper path to the process list file')
        file_name = f'{Register.register_directory_name}/{proc_name}.list'
        full_command = Process.Create_Full_Command(
            proc_name, command_list)
        if(debug_moode):
            print(f'Full command: {full_command}')
        with open(file_name, 'w+'):
            try:
                Process.Save_Process_Output(
                    full_command, file_name)
            except Exception as exc:
                print(f'Error: {exc}')

    @ classmethod
    def Clean_Register_Directory(cls):
        dirr = Register.register_directory_name
        if(os.path.isdir(dirr)):
            files = os.listdir(dirr)
            if(len(files) > 0):
                for file in files:
                    try:
                        os.remove(
                            f'{Register.register_directory_name}/{os.path.relpath(file)}')
                    except Exception as err:
                        print(
                            f'Could not remove the file from the process register!\nReason: {err}')
                # print('Process register empty. Skipping the cleaning procedure')
                pass


process_list = ['logstash', 'ssh', 'python', 'bash', 'code']


class Utils():
    """functions that are used for monitoring running processes, and any occuring instances within the process tree"""

    process_table = 'process.table'

    @classmethod
    def Watch_Process_Register(cls, register, execution_time):
        runtime = True

        start_time = time.time()
        if(runtime):
            print('Watching register')

        # start the monitoring process
        while(runtime):
            print(f'watching...')

            # count the running instances for each process that exists in the registry
            for process in register:
                print(process)

            if(time.time() - start_time >= execution_time):
                runtime = False
                break

    @classmethod
    def Pull_Processes(cls, process_table):
        try:
            with open(process_table, 'r+') as table:
                process_list = table.readlines()
        except FileNotFoundError:
            return -1

        # clean the list
        cleaned_list = [str(x).strip() for x in process_list]
        return cleaned_list


yy = Utils.Pull_Processes(Utils.process_table)
print(yy)


# if(__name__ == '__main__'):
#     # creating the directory where each instance of a process will be saved as a file
#     Register.Create_Register_Directory(Register.register_directory_name)

#     runtime = True
#     clean_up = False

#     total_execution_time = 5

#     proc_name = 'logstash'

#     itx = 1
#     print(f'Starting iterations...')

#     start_time = time.time()
#     while(runtime):
#         print(f'Iteration {itx}...')
#         for monitored_process in process_list:
#             Register.Create_File_Register(
#                 monitored_process, Process.process_getter_command)
#         if(int(time.time() - start_time) < total_execution_time):
#             time.sleep(1)
#         else:
#             runtime = False
#         itx += 1

#     process_instances = Process.Count_Running_Instances(proc_name)
#     print(f'There are {process_instances}-{proc_name} instances running...')

#     if(clean_up):
#         print('Doing cleanup')
#         # cleaning up the register
#         # removing the files in which all running processes are stored
#         Register.Clean_Register_Directory()
