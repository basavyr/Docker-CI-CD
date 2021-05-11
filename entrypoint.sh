#!/usr/bin/env bash
pythonAppPath='py/get_process/'
pythonApp='py_process.py'
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
zip -r $releaseApp.zip $pythonAppPath