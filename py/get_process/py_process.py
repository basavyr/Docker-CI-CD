#!/usr/bin/env python
import psutil


class Process:
    # save the processes to a file for later usage
    process_list = 'plist.dat'

    @classmethod
    def Check_Process_Exists(cls, process_list, process_name):
        p_list = []
        for proc in psutil.process_iter():
            try:
                proc_name = str(proc.name()).lower()
                proc_id = proc.pid
                p_list.append(f'{proc_name}:::{proc_id}')
            except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return p_list

    @classmethod
    def Create_Process_List(cls, process_list):
        with open(process_list, 'w+') as writer:
            for proc in psutil.process_iter():
                try:
                    processName = str(proc.name()).lower()
                    processID = proc.pid
                    proc_exe = proc.exe()
                    writer.write(f'{processName}:::{processID}:::{proc_exe}\n')
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        return 1


if __name__ == '__main__':
    proc = Process()
    proc.Create_Process_List(proc.process_list)
    print('Running the processes app.')
    print(f'The processes are saved into {proc.process_list}')
