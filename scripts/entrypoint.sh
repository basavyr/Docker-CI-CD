#!/bin/bash
echo 'Setting up the PATH for using pyenv and pipenv'
export PATH="/root/.pyenv/plugins/pyenv-virtualenv/shims:/root/.pyenv/shims:/root/.pyenv/bin:$PATH"
echo 'Setting up the LANG var'
export LC_ALL=C
export LANG="C.UTF-8"
echo 'Checking services'
python --version
pyenv versions
pyenv global