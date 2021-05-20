#!/usr/bin/env bash
pythonAppPath='py/py_subprocess/'
pythonApp='piped_process.py'
releaseApp='process_app'
export LANG=en_US.UTF8

cd $pythonAppPath
echo 'Setting up the virtual environment'
pyenv local systems
echo 'Installing packages and generating lockfile'
pipenv install

echo 'Running the python application within the current virtualenv'
pipenv run python $pythonApp
cd $HOME
ls -l
zip -r $releaseApp.zip $pythonAppPath
ls -l