#!/bin/bash
echo 'Setting up the PATH for using pyenv and pipenv'
export PATH="/root/.pyenv/plugins/pyenv-virtualenv/shims:/root/.pyenv/shims:/root/.pyenv/bin:$PATH"
echo 'Setting up the LANG var'
export LC_ALL=C
export LANG="C.UTF-8"
echo 'Creating the log file within the shell script'
touch /var/log/dfcti_system_logs.log
chmod +x /var/log/dfcti_system_logs.log 
echo 'Installing the required packages'
cd py/log_writing
pyenv local systems
pipenv install
echo 'Starting the log-writer procedure'
pipenv run python write.py 10
