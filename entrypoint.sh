#!/bin/bash
export PATH="/root/.pyenv/plugins/pyenv-virtualenv/shims:/root/.pyenv/shims:/root/.pyenv/bin:$PATH"
echo 'Creating the log file within the shell script'
touch /var/log/dfcti_system_logs.log
chmod 770 /var/log/dfcti_system_logs.log 
echo 'Starting the log-writer procedure'
cd py/log_writing
pyenv local systems
pipenv install
pipenv run python write.py 10