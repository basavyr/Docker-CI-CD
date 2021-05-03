#!/bin/bash
export PATH="/root/.pyenv/plugins/pyenv-virtualenv/shims:/root/.pyenv/shims:/root/.pyenv/bin:$PATH"
cd py/numpy_test
pyenv local systems
pipenv install
pipenv run python test.py
tree -h
