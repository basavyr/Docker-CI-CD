#!/usr/bin/env python
import subprocess


# for shell=False use absolute paths
p = subprocess.Popen("ps aux | grep zsh", shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

output = 'results.out'

p_stdout = p.stdout.read()
p_stderr = p.stderr.read()

decoder = lambda x: x.decode('UTF-8')


with open(output, 'w+') as save:
    save.write(decoder(p_stdout))


class Piped_Process:

    def __init__(self, command_list):
        if(len(command_list) == 1):
            self.piped_command = f'{command_list[0]}'
        else:
            piped_command = f''
            cmd_idx = 0
            for cmd in command_list:
                if(cmd_idx == 0):
                    piped_command = cmd
                else:
                    piped_command = piped_command + ' | ' + cmd
                cmd_idx += 1
            self.piped_command = piped_command

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


command_list = ['ls -la', 'grep  dat']

piped = Piped_Process.Run_Process(command_list)
if(piped[1] != b''):
    print('😭')
else:
    print('🥰')
