#!/bin/bash
export PATH="/root/.pyenv/plugins/pyenv-virtualenv/shims:/root/.pyenv/shims:/root/.pyenv/bin:$PATH"
cd py/log_writing
pyenv local systems
pipenv install
pipenv run python write.py 10